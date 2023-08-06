#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

import os.path
import platform
import signal
import sys
import socket
import configobj
import logging
import sentry_sdk
import time
from . import services
from . import events
from . import device
from . import simulator
from . import acurite
from . import vantage


class InitializationError(Exception):
    pass


class Engine(object):
    """The main engine responsible for the creating and dispatching of events
    from the weather station.

    When a service loads, it binds callbacks to events. When an event occurs,
    the bound callback will be called."""

    def __init__(self, config_dict, additional_services=None):
        timeout = int(config_dict.get('socket_timeout', 20))
        socket.setdefaulttimeout(timeout)

        self.callbacks = dict()
        self.service_obj = []
        self.setupStation(config_dict)
        self.loadServices(config_dict, additional_services)

    def setupStation(self, config_dict):
        """Set up the weather station hardware."""

        stationType = config_dict['Station']['station_type']

        driver_info_dict = {
            'Vantage': vantage.loader,
            'AcuRite': acurite.loader,
            'Simulator': simulator.loader
        }

        loader = driver_info_dict[stationType]

        logging.info("engine: Loading station type %s" % stationType)

        try:
            self.console = loader(config_dict)
        except Exception as ex:
            raise InitializationError(ex)

    def loadServices(self, config_dict, additional_services):
        try:
            self.service_obj.append(services.QC(self, config_dict))
            self.service_obj.append(services.Wunderground(self, config_dict))
            self.service_obj.append(services.Nimbus(self, config_dict))
            self.service_obj.append(services.Print(self, config_dict))
            self.service_obj.append(services.GC(self, config_dict))
            self.service_obj.append(services.Sentinel(self, config_dict))

            if additional_services is not None:
                for service in additional_services:
                    self.service_obj.append(service(self, config_dict))

        except Exception:
            self.shutDown()
            raise

    def run(self):
        try:
            self.dispatchEvent(events.Event(events.STARTUP))

            logging.info("engine: Starting main packet loop.")

            while True:
                try:
                    self.dispatchEvent(events.Event(events.PRE_LOOP))
                    for packet in self.console.genLoopPackets():
                        self.dispatchEvent(events.Event(events.NEW_LOOP_PACKET, packet=packet))
                except events.BreakLoop:
                    pass

            logging.error("engine: Internal error. Packet loop has exited.")

        finally:
            logging.info("engine: Main loop exiting. Shutting engine down.")
            self.shutDown()

    def bind(self, event_type, callback):
        """Binds an event to a callback function."""

        self.callbacks.setdefault(event_type, []).append(callback)

    def dispatchEvent(self, event):
        """Call all registered callbacks for an event."""

        if event.event_type in self.callbacks:
            for callback in self.callbacks[event.event_type]:
                callback(event)

    def shutDown(self):
        """Run when an engine shutdown is requested."""

        if hasattr(self, 'service_obj'):
            while len(self.service_obj):
                try:
                    self.service_obj[-1].shutDown()
                except BaseException:
                    pass
                del self.service_obj[-1]

            del self.service_obj

        try:
            del self.callbacks
        except AttributeError:
            pass

        try:
            self.console.closePort()
            del self.console
        except BaseException:
            pass


class Restart(Exception):
    """Exception thrown when restarting the engine is desired."""


def sigHUPhandler(dummy_signum, dummy_frame):
    logging.info("engine: Received signal HUP. Initiating restart.")
    raise Restart


class Terminate(Exception):
    """Exception thrown when terminating the engine."""


def sigTERMhandler(dummy_signum, dummy_frame):
    logging.info("engine: Received signal TERM.")
    raise Terminate


def main():
    """Prepare the main loop and run it.

    Mostly consists of a bunch of high-level preparatory calls, protected
    by try blocks in the case of an exception."""

    config_dict = getConfiguration("/etc/nimbus/nimbus.conf")

    log_level = logging.INFO

    if int(config_dict.get('debug', 0)):
        log_level = logging.DEBUG

    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=log_level, force=True)

    if 'sentry_dsn' in config_dict:
        logging.info("engine: Initializing sentry with dsn %s" % config_dict['sentry_dsn'])
        sentry_sdk.init(config_dict['sentry_dsn'])

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    signal.signal(signal.SIGHUP, sigHUPhandler)
    signal.signal(signal.SIGTERM, sigTERMhandler)

    logging.info("engine: Initializing nimbus")
    logging.info("engine: Using Python %s" % sys.version)
    logging.info("engine: Platform %s" % platform.platform())

    cwd = os.getcwd()

    while True:

        os.chdir(cwd)

        try:
            logging.info("engine: Initializing engine")

            engine = Engine(config_dict)

            logging.info("engine: Starting up nimbus")

            engine.run()

            logging.error("engine: Unexpected exit from main loop. Program exiting.")

        except InitializationError as e:
            logging.error("engine: Unable to load driver: %s" % e)
            logging.info("    ****  Waiting 60 seconds then retrying...")
            time.sleep(60)
            logging.info("engine: retrying...")

        except device.WeeWxIOError as e:
            logging.critical("engine: Caught WeeWxIOError: %s" % e)
            logging.critical("    ****  Waiting 60 seconds then retrying...")
            time.sleep(60)
            logging.info("engine: retrying...")

        except OSError as e:
            logging.critical("engine: Caught OSError: %s" % e)
            logging.critical("****  Waiting 10 seconds then retrying...")
            time.sleep(10)
            logging.info("engine: retrying...")

        except Restart:
            logging.info("engine: Received signal HUP. Restarting.")

        except Terminate:
            logging.info("engine: Terminating nimbus version")
            sys.exit()

        except KeyboardInterrupt:
            logging.critical("engine: Keyboard interrupt.")
            raise

        except Exception as ex:
            logging.critical("engine: Caught unrecoverable exception in engine: %s" % ex)
            logging.critical("****  Exiting.")
            raise


def getConfiguration(config_path):
    """Return the configuration file at the given path."""

    try:
        config_dict = configobj.ConfigObj(config_path, file_error=True)
    except IOError:
        logging.critical("engine: Unable to open configuration file %s" % config_path)
        raise
    except configobj.ConfigObjError as e:
        logging.critical("engine: Error while parsing configuration file %s" % config_path)
        logging.critical("****    Reason: '%s'" % e)
        raise

    logging.info("engine: Using configuration file %s" % config_path)

    return config_dict
