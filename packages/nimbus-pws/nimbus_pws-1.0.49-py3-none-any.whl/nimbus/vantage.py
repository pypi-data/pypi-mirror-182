#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

import datetime
import logging
import struct
import time

import six
from six import indexbytes, byte2int
from six.moves import zip
from functools import reduce
from . import device


log = logging.getLogger(__name__)

DRIVER_NAME = 'Vantage'
DRIVER_VERSION = '3.4.0'


def to_int(x):
    """Convert an object to an integer, unless it is None

    Examples:
    >>> print(to_int(123))
    123
    >>> print(to_int('123'))
    123
    >>> print(to_int(-5.2))
    -5
    >>> print(to_int(None))
    None
    """
    if isinstance(x, six.string_types) and x.lower() == 'none':
        x = None
    try:
        return int(x) if x is not None else None
    except ValueError:
        # Perhaps it's a string, holding a floating point number?
        return int(float(x))

_table=[
0x0000,  0x1021,  0x2042,  0x3063,  0x4084,  0x50a5,  0x60c6,  0x70e7,  # 0x00
0x8108,  0x9129,  0xa14a,  0xb16b,  0xc18c,  0xd1ad,  0xe1ce,  0xf1ef,  # 0x08
0x1231,  0x0210,  0x3273,  0x2252,  0x52b5,  0x4294,  0x72f7,  0x62d6,  # 0x10
0x9339,  0x8318,  0xb37b,  0xa35a,  0xd3bd,  0xc39c,  0xf3ff,  0xe3de,  # 0x18
0x2462,  0x3443,  0x0420,  0x1401,  0x64e6,  0x74c7,  0x44a4,  0x5485,  # 0x20
0xa56a,  0xb54b,  0x8528,  0x9509,  0xe5ee,  0xf5cf,  0xc5ac,  0xd58d,  # 0x28
0x3653,  0x2672,  0x1611,  0x0630,  0x76d7,  0x66f6,  0x5695,  0x46b4,  # 0x30
0xb75b,  0xa77a,  0x9719,  0x8738,  0xf7df,  0xe7fe,  0xd79d,  0xc7bc,  # 0x38
0x48c4,  0x58e5,  0x6886,  0x78a7,  0x0840,  0x1861,  0x2802,  0x3823,  # 0x40
0xc9cc,  0xd9ed,  0xe98e,  0xf9af,  0x8948,  0x9969,  0xa90a,  0xb92b,  # 0x48
0x5af5,  0x4ad4,  0x7ab7,  0x6a96,  0x1a71,  0x0a50,  0x3a33,  0x2a12,  # 0x50
0xdbfd,  0xcbdc,  0xfbbf,  0xeb9e,  0x9b79,  0x8b58,  0xbb3b,  0xab1a,  # 0x58
0x6ca6,  0x7c87,  0x4ce4,  0x5cc5,  0x2c22,  0x3c03,  0x0c60,  0x1c41,  # 0x60
0xedae,  0xfd8f,  0xcdec,  0xddcd,  0xad2a,  0xbd0b,  0x8d68,  0x9d49,  # 0x68
0x7e97,  0x6eb6,  0x5ed5,  0x4ef4,  0x3e13,  0x2e32,  0x1e51,  0x0e70,  # 0x70
0xff9f,  0xefbe,  0xdfdd,  0xcffc,  0xbf1b,  0xaf3a,  0x9f59,  0x8f78,  # 0x78
0x9188,  0x81a9,  0xb1ca,  0xa1eb,  0xd10c,  0xc12d,  0xf14e,  0xe16f,  # 0x80
0x1080,  0x00a1,  0x30c2,  0x20e3,  0x5004,  0x4025,  0x7046,  0x6067,  # 0x88
0x83b9,  0x9398,  0xa3fb,  0xb3da,  0xc33d,  0xd31c,  0xe37f,  0xf35e,  # 0x90
0x02b1,  0x1290,  0x22f3,  0x32d2,  0x4235,  0x5214,  0x6277,  0x7256,  # 0x98
0xb5ea,  0xa5cb,  0x95a8,  0x8589,  0xf56e,  0xe54f,  0xd52c,  0xc50d,  # 0xA0
0x34e2,  0x24c3,  0x14a0,  0x0481,  0x7466,  0x6447,  0x5424,  0x4405,  # 0xA8
0xa7db,  0xb7fa,  0x8799,  0x97b8,  0xe75f,  0xf77e,  0xc71d,  0xd73c,  # 0xB0
0x26d3,  0x36f2,  0x0691,  0x16b0,  0x6657,  0x7676,  0x4615,  0x5634,  # 0xB8
0xd94c,  0xc96d,  0xf90e,  0xe92f,  0x99c8,  0x89e9,  0xb98a,  0xa9ab,  # 0xC0
0x5844,  0x4865,  0x7806,  0x6827,  0x18c0,  0x08e1,  0x3882,  0x28a3,  # 0xC8
0xcb7d,  0xdb5c,  0xeb3f,  0xfb1e,  0x8bf9,  0x9bd8,  0xabbb,  0xbb9a,  # 0xD0
0x4a75,  0x5a54,  0x6a37,  0x7a16,  0x0af1,  0x1ad0,  0x2ab3,  0x3a92,  # 0xD8
0xfd2e,  0xed0f,  0xdd6c,  0xcd4d,  0xbdaa,  0xad8b,  0x9de8,  0x8dc9,  # 0xE0
0x7c26,  0x6c07,  0x5c64,  0x4c45,  0x3ca2,  0x2c83,  0x1ce0,  0x0cc1,  # 0xE8
0xef1f,  0xff3e,  0xcf5d,  0xdf7c,  0xaf9b,  0xbfba,  0x8fd9,  0x9ff8,  # 0xF0
0x6e17,  0x7e36,  0x4e55,  0x5e74,  0x2e93,  0x3eb2,  0x0ed1,  0x1ef0   # 0xF8
]


def crc16(bytes, crc_start=0):
    """ Calculate CRC16 sum"""

    # We need something that returns integers when iterated over.
    try:
        # Python 2
        byte_iter = [ord(x) for x in bytes]
    except TypeError:
        # Python 3
        byte_iter = bytes

    crc_sum = reduce(lambda crc, ch : (_table[(crc >> 8) ^ ch] ^ (crc << 8)) & 0xffff, byte_iter, crc_start)

    return crc_sum


def loader(config_dict):
    return Vantage(**config_dict[DRIVER_NAME])


# A few handy constants:
_ack = b'\x06'
_resend = b'\x15'  # NB: The Davis documentation gives this code as 0x21, but it's actually decimal 21


# ===============================================================================
#                           class BaseWrapper
# ===============================================================================

class BaseWrapper(object):
    """Base class for (Serial|Ethernet)Wrapper"""

    def __init__(self, wait_before_retry, command_delay):

        self.wait_before_retry = wait_before_retry
        self.command_delay = command_delay

    def read(self, nbytes=1):
        raise NotImplementedError

    def write(self, buf):
        raise NotImplementedError

    def flush_input(self):
        raise NotImplementedError

    # ===============================================================================
    #          Primitives for working with the Davis Console
    # ===============================================================================

    def wakeup_console(self, max_tries=3):
        """Wake up a Davis Vantage console.

        This call has three purposes:
        1. Wake up a sleeping console;
        2. Cancel pending LOOP data (if any);
        3. Flush the input buffer
           Note: a flushed buffer is important before sending a command; we want to make sure
           the next received character is the expected ACK.

        If unsuccessful, an exception of type weewx.WakeupError is thrown"""

        for count in range(max_tries):
            try:
                # Wake up console and cancel pending LOOP data.
                # First try a gentle wake up
                self.write(b'\n')
                _resp = self.read(2)
                if _resp == b'\n\r':  # LF, CR = 0x0a, 0x0d
                    # We're done; the console accepted our cancel LOOP command; nothing to flush
                    log.debug("Gentle wake up of console successful")
                    return
                # That didn't work. Try a rude wake up.
                # Flush any pending LOOP packets
                self.flush_input()
                # Look for the acknowledgment of the sent '\n'
                _resp = self.read(2)
                if _resp == b'\n\r':
                    log.debug("Rude wake up of console successful")
                    return
            except device.WeeWxIOError as e:
                log.debug("Wakeup retry #%d failed: %s", count + 1, e)
                print("Unable to wake up Vantage console... sleeping")
                time.sleep(self.wait_before_retry)
                print("Unable to wake up Vantage console... retrying")

        log.error("Unable to wake up Vantage console")
        raise device.WakeupError("Unable to wake up Vantage console")

    def send_data(self, data):
        """Send data to the Davis console, waiting for an acknowledging <ACK>

        If the <ACK> is not received, no retry is attempted. Instead, an exception
        of type weewx.WeeWxIOError is raised

        data: The data to send, as a byte string"""

        self.write(data)

        # Look for the acknowledging ACK character
        _resp = self.read()
        if _resp != _ack:
            log.error("No <ACK> received from Vantage console")
            raise device.WeeWxIOError("No <ACK> received from Vantage console")

    def send_data_with_crc16(self, data, max_tries=3):
        """Send data to the Davis console along with a CRC check, waiting for an acknowledging <ack>.
        If none received, resend up to max_tries times.

        data: The data to send, as a byte string"""

        # Calculate the crc for the data:
        _crc = crc16(data)

        # ...and pack that on to the end of the data in big-endian order:
        _data_with_crc = data + struct.pack(">H", _crc)

        # Retry up to max_tries times:
        for count in range(max_tries):
            try:
                self.write(_data_with_crc)
                # Look for the acknowledgment.
                _resp = self.read()
                if _resp == _ack:
                    return
            except device.WeeWxIOError as e:
                log.debug("send_data_with_crc16; try #%d: %s", count + 1, e)

        log.error("Unable to pass CRC16 check while sending data to Vantage console")
        raise device.CRCError("Unable to pass CRC16 check while sending data to Vantage console")

    def send_command(self, command, max_tries=3):
        """Send a command to the console, then look for the byte string 'OK' in the response.

        Any response from the console is split on \n\r characters and returned as a list."""

        for count in range(max_tries):
            try:
                self.wakeup_console(max_tries=max_tries)

                self.write(command)
                # Takes some time for the Vantage to react and fill up the buffer. Sleep for a bit:
                time.sleep(self.command_delay)
                # Can't use function serial.readline() because the VP responds with \n\r,
                # not just \n. So, instead find how many bytes are waiting and fetch them all
                nc = self.queued_bytes()
                _buffer = self.read(nc)
                # Split the buffer on the newlines
                _buffer_list = _buffer.strip().split(b'\n\r')
                # The first member should be the 'OK' in the VP response
                if _buffer_list[0] == b'OK':
                    # Return the rest:
                    return _buffer_list[1:]

            except device.WeeWxIOError as e:
                # Caught an error. Log, then keep trying...
                log.debug("send_command; try #%d failed: %s", count + 1, e)

        msg = "Max retries exceeded while sending command %s" % command
        log.error(msg)
        raise device.RetriesExceeded(msg)

    def get_data_with_crc16(self, nbytes, prompt=None, max_tries=3):
        """Get a packet of data and do a CRC16 check on it, asking for retransmit if necessary.

        It is guaranteed that the length of the returned data will be of the requested length.
        An exception of type CRCError will be thrown if the data cannot pass the CRC test
        in the requested number of retries.

        nbytes: The number of bytes (including the 2 byte CRC) to get.

        prompt: Any string to be sent before requesting the data. Default=None

        max_tries: Number of tries before giving up. Default=3

        returns: the packet data as a byte string. The last 2 bytes will be the CRC"""
        if prompt:
            self.write(prompt)

        first_time = True
        _buffer = b''

        for count in range(max_tries):
            try:
                if not first_time:
                    self.write(_resend)
                _buffer = self.read(nbytes)
                if crc16(_buffer) == 0:
                    return _buffer
                log.debug("Get_data_with_crc16; try #%d failed. CRC error", count + 1)
            except device.WeeWxIOError as e:
                log.debug("Get_data_with_crc16; try #%d failed: %s", count + 1, e)
            first_time = False

        if _buffer:
            log.error("Unable to pass CRC16 check while getting data")
            raise device.CRCError("Unable to pass CRC16 check while getting data")
        else:
            log.debug("Timeout in get_data_with_crc16")
            raise device.WeeWxIOError("Timeout in get_data_with_crc16")


# ===============================================================================
#                           class Serial Wrapper
# ===============================================================================

def guard_termios(fn):
    """Decorator function that converts termios exceptions into weewx exceptions."""
    # Some functions in the module 'serial' can raise undocumented termios
    # exceptions. This catches them and converts them to weewx exceptions.
    try:
        import termios
        def guarded_fn(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except termios.error as e:
                raise device.WeeWxIOError(e)
    except ImportError:
        def guarded_fn(*args, **kwargs):
            return fn(*args, **kwargs)
    return guarded_fn


class SerialWrapper(BaseWrapper):
    """Wraps a serial connection returned from package serial"""

    def __init__(self, port, baudrate, timeout, wait_before_retry, command_delay):
        super(SerialWrapper, self).__init__(wait_before_retry=wait_before_retry,
                                            command_delay=command_delay)
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    @guard_termios
    def flush_input(self):
        self.serial_port.flushInput()

    @guard_termios
    def flush_output(self):
        self.serial_port.flushOutput()

    @guard_termios
    def queued_bytes(self):
        return self.serial_port.inWaiting()

    def read(self, chars=1):
        import serial
        try:
            _buffer = self.serial_port.read(chars)
        except serial.serialutil.SerialException as e:
            log.error("SerialException on read.")
            log.error("   ****  %s", e)
            log.error("   ****  Is there a competing process running??")
            # Reraise as a Weewx error I/O error:
            raise device.WeeWxIOError(e)
        N = len(_buffer)
        if N != chars:
            raise device.WeeWxIOError("Expected to read %d chars; got %d instead" % (chars, N))
        return _buffer

    def write(self, data):
        import serial
        try:
            N = self.serial_port.write(data)
        except serial.serialutil.SerialException as e:
            log.error("SerialException on write.")
            log.error("   ****  %s", e)
            # Reraise as a Weewx error I/O error:
            raise device.WeeWxIOError(e)
        # Python version 2.5 and earlier returns 'None', so it cannot be used to test for completion.
        if N is not None and N != len(data):
            raise device.WeeWxIOError("Expected to write %d chars; sent %d instead" % (len(data), N))

    def openPort(self):
        import serial
        # Open up the port and store it
        self.serial_port = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        log.debug("Opened up serial port %s; baud %d; timeout %.2f", self.port, self.baudrate, self.timeout)

    def closePort(self):
        try:
            # This will cancel any pending loop:
            self.write(b'\n')
        except:
            pass
        self.serial_port.close()


# ===============================================================================
#                           class EthernetWrapper
# ===============================================================================

class EthernetWrapper(BaseWrapper):
    """Wrap a socket"""

    def __init__(self, host, port, timeout, tcp_send_delay, wait_before_retry, command_delay):

        super(EthernetWrapper, self).__init__(wait_before_retry=wait_before_retry,
                                              command_delay=command_delay)

        self.host = host
        self.port = port
        self.timeout = timeout
        self.tcp_send_delay = tcp_send_delay

    def openPort(self):
        import socket
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
        except (socket.error, socket.timeout, socket.herror) as ex:
            log.error("Socket error while opening port %d to ethernet host %s.", self.port, self.host)
            # Reraise as a weewx I/O error:
            raise device.WeeWxIOError(ex)
        except:
            log.error("Unable to connect to ethernet host %s on port %d.", self.host, self.port)
            raise
        log.debug("Opened up ethernet host %s on port %d. timeout=%s, tcp_send_delay=%s",
                  self.host, self.port, self.timeout, self.tcp_send_delay)

    def closePort(self):
        import socket
        try:
            # This will cancel any pending loop:
            self.write(b'\n')
        except:
            pass
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def flush_input(self):
        """Flush the input buffer from WeatherLinkIP"""
        import socket
        try:
            # This is a bit of a hack, but there is no analogue to pyserial's flushInput()
            # Set socket timeout to 0 to get immediate result
            self.socket.settimeout(0)
            self.socket.recv(4096)
        except (socket.timeout, socket.error):
            pass
        finally:
            # set socket timeout back to original value
            self.socket.settimeout(self.timeout)

    def flush_output(self):
        """Flush the output buffer to WeatherLinkIP

        This function does nothing as there should never be anything left in
        the buffer when using socket.sendall()"""
        pass

    def queued_bytes(self):
        """Determine how many bytes are in the buffer"""
        import socket
        length = 0
        try:
            self.socket.settimeout(0)
            length = len(self.socket.recv(8192, socket.MSG_PEEK))
        except socket.error:
            pass
        finally:
            self.socket.settimeout(self.timeout)
        return length

    def read(self, chars=1):
        """Read bytes from WeatherLinkIP"""
        import socket
        _buffer = b''
        _remaining = chars
        while _remaining:
            _N = min(4096, _remaining)
            try:
                _recv = self.socket.recv(_N)
            except (socket.timeout, socket.error) as ex:
                log.error("ip-read error: %s", ex)
                # Reraise as a weewx I/O error:
                raise device.WeeWxIOError(ex)
            _nread = len(_recv)
            if _nread == 0:
                raise device.WeeWxIOError("Expected %d characters; got zero instead" % (_N,))
            _buffer += _recv
            _remaining -= _nread
        return _buffer

    def write(self, data):
        """Write to a WeatherLinkIP"""
        import socket
        try:
            self.socket.sendall(data)
            # A delay of 0.0 gives socket write error; 0.01 gives no ack error; 0.05 is OK for weewx program
            # Note: a delay of 0.5 s is required for wee_device --logger=logger_info
            time.sleep(self.tcp_send_delay)
        except (socket.timeout, socket.error) as ex:
            log.error("ip-write error: %s", ex)
            # Reraise as a weewx I/O error:
            raise device.WeeWxIOError(ex)


# ===============================================================================
#                           class Vantage
# ===============================================================================

class Vantage(device.AbstractDevice):
    """Class that represents a connection to a Davis Vantage console.

    The connection to the console will be open after initialization"""

    # Various codes used internally by the VP2:
    barometer_unit_dict = {0: 'inHg', 1: 'mmHg', 2: 'hPa', 3: 'mbar'}
    temperature_unit_dict = {0: 'degree_F', 1: 'degree_10F', 2: 'degree_C', 3: 'degree_10C'}
    altitude_unit_dict = {0: 'foot', 1: 'meter'}
    rain_unit_dict = {0: 'inch', 1: 'mm'}
    wind_unit_dict = {0: 'mile_per_hour', 1: 'meter_per_second', 2: 'km_per_hour', 3: 'knot'}
    wind_cup_dict = {0: 'small', 1: 'large'}
    rain_bucket_dict = {0: '0.01 inches', 1: '0.2 mm', 2: '0.1 mm'}
    transmitter_type_dict = {0: 'iss', 1: 'temp', 2: 'hum', 3: 'temp_hum', 4: 'wind',
                             5: 'rain', 6: 'leaf', 7: 'soil', 8: 'leaf_soil',
                             9: 'sensorlink', 10: 'none'}
    repeater_dict = {0: 'none', 1: 'A', 2: 'B', 3: 'C', 4: 'D',
                     5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    listen_dict = {0: 'inactive', 1: 'active'}

    def __init__(self, **vp_dict):
        """Initialize an object of type Vantage.

        NAMED ARGUMENTS:

        connection_type: The type of connection (serial|ethernet) [Required]

        port: The serial port of the VP. [Required if serial/USB
        communication]

        host: The Vantage network host [Required if Ethernet communication]

        baudrate: Baudrate of the port. [Optional. Default 19200]

        tcp_port: TCP port to connect to [Optional. Default 22222]

        tcp_send_delay: Block after sending data to WeatherLinkIP to allow it
        to process the command [Optional. Default is 0.5]

        timeout: How long to wait before giving up on a response from the
        serial port. [Optional. Default is 4]

        wait_before_retry: How long to wait before retrying. [Optional.
        Default is 1.2 seconds]

        command_delay: How long to wait after sending a command before looking
        for acknowledgement. [Optional. Default is 0.5 seconds]

        max_tries: How many times to try again before giving up. [Optional.
        Default is 4]

        iss_id: The station number of the ISS [Optional. Default is 1]

        model_type: Vantage Pro model type. 1=Vantage Pro; 2=Vantage Pro2
        [Optional. Default is 2]

        loop_request: Requested packet type. 1=LOOP; 2=LOOP2; 3=both.

        loop_batch: How many LOOP packets to get in a single  batch.
        [Optional. Default is 200]

        max_batch_errors: How many errors to allow in a batch before a restart.
        [Optional. Default is 3]
        """

        log.debug('Driver version is %s', DRIVER_VERSION)

        self.hardware_type = None

        # These come from the configuration dictionary:
        self.max_tries = to_int(vp_dict.get('max_tries', 4))
        self.iss_id = to_int(vp_dict.get('iss_id'))
        self.model_type = to_int(vp_dict.get('model_type', 2))
        if self.model_type not in (1, 2):
            raise device.UnsupportedFeature("Unknown model_type (%d)" % self.model_type)
        self.loop_request = to_int(vp_dict.get('loop_request', 1))
        log.debug("Option loop_request=%d", self.loop_request)
        self.loop_batch = to_int(vp_dict.get('loop_batch', 200))
        self.max_batch_errors = to_int(vp_dict.get('max_batch_errors', 3))

        self.save_day_rain = None
        self.max_dst_jump = 7200

        # Get an appropriate port, depending on the connection type:
        self.port = Vantage._port_factory(vp_dict)

        # Open it up:
        self.port.openPort()

        # Read the EEPROM and fill in properties in this instance
        self._setup()

    def openPort(self):
        """Open up the connection to the console"""
        self.port.openPort()

    def closePort(self):
        """Close the connection to the console. """
        self.port.closePort()

    def genLoopPackets(self):
        """Generator function that returns loop packets"""

        while True:
            # Get LOOP packets in big batches This is necessary because there is
            # an undocumented limit to how many LOOP records you can request
            # on the VP (somewhere around 220).
            for _loop_packet in self.genDavisLoopPackets(self.loop_batch):
                yield _loop_packet

    def genDavisLoopPackets(self, N=1):
        """Generator function to return N loop packets from a Vantage console

        N: The number of packets to generate [default is 1]

        yields: up to N loop packets (could be less in the event of a
        read or CRC error).
        """

        log.debug("Requesting %d LOOP packets.", N)

        attempt = 1
        while attempt <= self.max_batch_errors:
            try:
                self.port.wakeup_console(self.max_tries)
                if self.loop_request == 1:
                    # If asking for old-fashioned LOOP1 data, send the older command in case the
                    # station does not support the LPS command:
                    self.port.send_data(b"LOOP %d\n" % N)
                else:
                    # Request N packets of type "loop_request":
                    self.port.send_data(b"LPS %d %d\n" % (self.loop_request, N))

                for loop in range(N):
                    loop_packet = self._get_packet()
                    yield loop_packet

            except device.WeeWxIOError as e:
                log.error("LOOP batch try #%d; error: %s", attempt, e)
                attempt += 1
        else:
            msg = "LOOP max batch errors (%d) exceeded." % self.max_batch_errors
            log.error(msg)
            raise device.RetriesExceeded(msg)

    def _get_packet(self):
        """Get a single LOOP packet"""
        # Fetch a packet...
        _buffer = self.port.read(99)
        # ... see if it passes the CRC test ...
        crc = crc16(_buffer)
        if crc:
            raise device.CRCError("LOOP buffer failed CRC check")
        # ... decode it ...
        loop_packet = self._unpackLoopPacket(_buffer[:95])
        # .. then return it
        return loop_packet

    def getTime(self):
        """Get the current time from the console, returning it as timestamp"""

        time_dt = self.getConsoleTime()
        return time.mktime(time_dt.timetuple())

    def getConsoleTime(self):
        """Return the raw time on the console, uncorrected for DST or timezone."""

        # Try up to max_tries times:
        for unused_count in range(self.max_tries):
            try:
                # Wake up the console...
                self.port.wakeup_console(max_tries=self.max_tries)
                # ... request the time...
                self.port.send_data(b'GETTIME\n')
                # ... get the binary data. No prompt, only one try:
                _buffer = self.port.get_data_with_crc16(8, max_tries=1)
                (sec, minute, hr, day, mon, yr, unused_crc) = struct.unpack("<bbbbbbH", _buffer)

                return datetime.datetime(yr + 1900, mon, day, hr, minute, sec)

            except device.WeeWxIOError:
                # Caught an error. Keep retrying...
                continue
        log.error("Max retries exceeded while getting time")
        raise device.RetriesExceeded("Max retries exceeded while getting time")

    def setTime(self):
        """Set the clock on the Davis Vantage console"""

        for unused_count in range(self.max_tries):
            try:
                # Wake the console and begin the setTime command
                self.port.wakeup_console(max_tries=self.max_tries)
                self.port.send_data(b'SETTIME\n')

                # Unfortunately, clock resolution is only 1 second, and transmission takes a
                # little while to complete, so round up the clock up. 0.5 for clock resolution
                # and 0.25 for transmission delay
                newtime_tt = time.localtime(int(time.time() + 0.75))

                # The Davis expects the time in reversed order, and the year is since 1900
                _buffer = struct.pack("<bbbbbb", newtime_tt[5], newtime_tt[4], newtime_tt[3], newtime_tt[2],
                                      newtime_tt[1], newtime_tt[0] - 1900)

                # Complete the setTime command
                self.port.send_data_with_crc16(_buffer, max_tries=1)
                return
            except device.WeeWxIOError:
                # Caught an error. Keep retrying...
                continue
        log.error("Max retries exceeded while setting time")
        raise device.RetriesExceeded("Max retries exceeded while setting time")

    def getStnTransmitters(self):
        """ Get the types of transmitters on the eight channels."""

        transmitters = []
        use_tx = self._getEEPROM_value(0x17)[0]
        transmitter_data = self._getEEPROM_value(0x19, "16B")

        for transmitter_id in range(8):
            transmitter_type = self.transmitter_type_dict[transmitter_data[transmitter_id * 2] & 0x0F]
            repeater = 0
            repeater = transmitter_data[transmitter_id * 2] & 0xF0
            repeater = (repeater >> 4) - 7 if repeater > 127 else 0
            transmitter = {"transmitter_type": transmitter_type,
                           "repeater": self.repeater_dict[repeater],
                           "listen": self.listen_dict[(use_tx >> transmitter_id) & 1]}
            if transmitter_type in ['temp', 'temp_hum']:
                # Extra temperature is origin 0.
                transmitter['temp'] = (transmitter_data[transmitter_id * 2 + 1] & 0xF) + 1
            if transmitter_type in ['hum', 'temp_hum']:
                # Extra humidity is origin 1.
                transmitter['hum'] = transmitter_data[transmitter_id * 2 + 1] >> 4
            transmitters.append(transmitter)
        return transmitters

    # ===========================================================================
    #              Davis Vantage utility functions
    # ===========================================================================

    @property
    def hardware_name(self):
        if self.hardware_type == 16:
            if self.model_type == 1:
                return "Vantage Pro"
            else:
                return "Vantage Pro2"
        elif self.hardware_type == 17:
            return "Vantage Vue"
        else:
            raise device.UnsupportedFeature("Unknown hardware type %d" % self.hardware_type)

    @property
    def archive_interval(self):
        return self.archive_interval_

    def _determine_hardware(self):
        # Determine the type of hardware:
        for count in range(self.max_tries):
            try:
                self.port.send_data(b"WRD\x12\x4d\n")
                self.hardware_type = byte2int(self.port.read())
                log.debug("Hardware type is %d", self.hardware_type)
                # 16 = Pro, Pro2, 17 = Vue
                return self.hardware_type
            except device.WeeWxIOError as e:
                log.error("_determine_hardware; retry #%d: '%s'", count, e)

        log.error("Unable to read hardware type; raise WeeWxIOError")
        raise device.WeeWxIOError("Unable to read hardware type")

    def _setup(self):
        """Retrieve the EEPROM data block from a VP2 and use it to set various properties"""

        self.port.wakeup_console(max_tries=self.max_tries)

        # Get hardware type, if not done yet.
        if self.hardware_type is None:
            self.hardware_type = self._determine_hardware()
            # Overwrite model_type if we have Vantage Vue.
            if self.hardware_type == 17:
                self.model_type = 2

        unit_bits = self._getEEPROM_value(0x29)[0]
        setup_bits = self._getEEPROM_value(0x2B)[0]
        self.rain_year_start = self._getEEPROM_value(0x2C)[0]
        self.archive_interval_ = self._getEEPROM_value(0x2D)[0] * 60
        self.altitude = self._getEEPROM_value(0x0F, "<h")[0]

        barometer_unit_code = unit_bits & 0x03
        temperature_unit_code = (unit_bits & 0x0C) >> 2
        altitude_unit_code = (unit_bits & 0x10) >> 4
        rain_unit_code = (unit_bits & 0x20) >> 5
        wind_unit_code = (unit_bits & 0xC0) >> 6

        self.wind_cup_type = (setup_bits & 0x08) >> 3
        self.rain_bucket_type = (setup_bits & 0x30) >> 4

        self.barometer_unit = Vantage.barometer_unit_dict[barometer_unit_code]
        self.temperature_unit = Vantage.temperature_unit_dict[temperature_unit_code]
        self.altitude_unit = Vantage.altitude_unit_dict[altitude_unit_code]
        self.rain_unit = Vantage.rain_unit_dict[rain_unit_code]
        self.wind_unit = Vantage.wind_unit_dict[wind_unit_code]
        self.wind_cup_size = Vantage.wind_cup_dict[self.wind_cup_type]
        self.rain_bucket_size = Vantage.rain_bucket_dict[self.rain_bucket_type]

        # Try to guess the ISS ID for gauging reception strength.
        if self.iss_id is None:
            stations = self.getStnTransmitters()
            # Wind retransmitter is best candidate.
            for station_id in range(0, 8):
                if stations[station_id]['transmitter_type'] == 'wind':
                    self.iss_id = station_id + 1  # Origin 1.
                    break
            else:
                # ISS is next best candidate.
                for station_id in range(0, 8):
                    if stations[station_id]['transmitter_type'] == 'iss':
                        self.iss_id = station_id + 1  # Origin 1.
                        break
                else:
                    # On Vue, can use VP2 ISS, which reports as "rain"
                    for station_id in range(0, 8):
                        if stations[station_id]['transmitter_type'] == 'rain':
                            self.iss_id = station_id + 1  # Origin 1.
                            break
                    else:
                        self.iss_id = 1  # Pick a reasonable default.

        log.debug("ISS ID is %s", self.iss_id)

    def _getEEPROM_value(self, offset, v_format="B"):
        """Return a list of values from the EEPROM starting at a specified offset, using a specified format"""

        nbytes = struct.calcsize(v_format)
        # Don't bother waking up the console for the first try. It's probably
        # already awake from opening the port. However, if we fail, then do a
        # wakeup.
        firsttime = True

        command = b"EEBRD %X %X\n" % (offset, nbytes)
        for unused_count in range(self.max_tries):
            try:
                if not firsttime:
                    self.port.wakeup_console(max_tries=self.max_tries)
                firsttime = False
                self.port.send_data(command)
                _buffer = self.port.get_data_with_crc16(nbytes + 2, max_tries=1)
                _value = struct.unpack(v_format, _buffer[:-2])
                return _value
            except device.WeeWxIOError:
                continue

        msg = "While getting EEPROM data value at address 0x%X" % offset
        log.error(msg)
        raise device.RetriesExceeded(msg)

    @staticmethod
    def _port_factory(vp_dict):
        """Produce a serial or ethernet port object"""

        timeout = float(vp_dict.get('timeout', 4.0))
        wait_before_retry = float(vp_dict.get('wait_before_retry', 1.2))
        command_delay = float(vp_dict.get('command_delay', 0.5))

        # Get the connection type. If it is not specified, assume 'serial':
        connection_type = vp_dict.get('type', 'serial').lower()

        if connection_type == "serial":
            port = vp_dict['port']
            baudrate = int(vp_dict.get('baudrate', 19200))
            return SerialWrapper(port, baudrate, timeout,
                                 wait_before_retry, command_delay)
        elif connection_type == "ethernet":
            hostname = vp_dict['host']
            tcp_port = int(vp_dict.get('tcp_port', 22222))
            tcp_send_delay = float(vp_dict.get('tcp_send_delay', 0.5))
            return EthernetWrapper(hostname, tcp_port, timeout, tcp_send_delay,
                                   wait_before_retry, command_delay)
        raise device.UnsupportedFeature(vp_dict['type'])

    def _unpackLoopPacket(self, raw_loop_buffer):
        """Decode a raw Davis LOOP packet, returning the results as a dictionary in physical units.

        raw_loop_buffer: The loop packet data buffer, passed in as
        a string (Python 2), or a byte array (Python 3).

        returns:

        A dictionary. The key will be an observation type, the value will be
        the observation in physical units."""

        # Get the packet type. It's in byte 4.
        packet_type = indexbytes(raw_loop_buffer, 4)
        if packet_type == 0:
            loop_struct = loop1_struct
            loop_types = loop1_types
        elif packet_type == 1:
            loop_struct = loop2_struct
            loop_types = loop2_types
        else:
            raise device.WeeWxIOError("Unknown LOOP packet type %s" % packet_type)

        # Unpack the data, using the appropriate compiled stuct.Struct buffer.
        # The result will be a long tuple with just the raw values from the console.
        data_tuple = loop_struct.unpack(raw_loop_buffer)

        # Combine it with the data types. The result will be a long iterable of 2-way
        # tuples: (type, raw-value)
        raw_loop_tuples = zip(loop_types, data_tuple)

        # Convert to a dictionary:
        raw_loop_packet = dict(raw_loop_tuples)
        # Add the bucket type. It's needed to decode rain bucket tips.
        raw_loop_packet['bucket_type'] = self.rain_bucket_type

        loop_packet = {
            'dateTime': int(time.time() + 0.5),
            'units': device.US
        }
        # Now we need to map the raw values to physical units.
        for _type in raw_loop_packet:
            if _type in extra_sensors and self.hardware_type == 17:
                # Vantage Vues do not support extra sensors. Skip them.
                continue
            # Get the mapping function for this type. If there is
            # no such function, supply a lambda function that returns None
            func = _loop_map.get(_type, lambda p, k: None)
            # Apply the function
            val = func(raw_loop_packet, _type)
            # Ignore None values:
            if val is not None:
                loop_packet[_type] = val

        # Because the Davis stations do not offer bucket tips in LOOP data, we
        # must calculate it by looking for changes in rain totals. This won't
        # work for the very first rain packet.
        if self.save_day_rain is None:
            delta = None
        else:
            delta = loop_packet['dayRain'] - self.save_day_rain
            # If the difference is negative, we're at the beginning of a month.
            if delta < 0: delta = None
        loop_packet['rain'] = delta
        self.save_day_rain = loop_packet['dayRain']

        return loop_packet

# ===============================================================================
#                                 LOOP packet
# ===============================================================================


# A list of all the types held in a Vantage LOOP packet in their native order.
loop1_schema = [
    ('loop', '3s'), ('rev_type', 'b'), ('packet_type', 'B'),
    ('next_record', 'H'), ('barometer', 'H'), ('inTemp', 'h'),
    ('inHumidity', 'B'), ('outTemp', 'h'), ('windSpeed', 'B'),
    ('windSpeed10', 'B'), ('windDir', 'H'), ('extraTemp1', 'B'),
    ('extraTemp2', 'B'), ('extraTemp3', 'B'), ('extraTemp4', 'B'),
    ('extraTemp5', 'B'), ('extraTemp6', 'B'), ('extraTemp7', 'B'),
    ('soilTemp1', 'B'), ('soilTemp2', 'B'), ('soilTemp3', 'B'),
    ('soilTemp4', 'B'), ('leafTemp1', 'B'), ('leafTemp2', 'B'),
    ('leafTemp3', 'B'), ('leafTemp4', 'B'), ('outHumidity', 'B'),
    ('extraHumid1', 'B'), ('extraHumid2', 'B'), ('extraHumid3', 'B'),
    ('extraHumid4', 'B'), ('extraHumid5', 'B'), ('extraHumid6', 'B'),
    ('extraHumid7', 'B'), ('rainRate', 'H'), ('UV', 'B'),
    ('radiation', 'H'), ('stormRain', 'H'), ('stormStart', 'H'),
    ('dayRain', 'H'), ('monthRain', 'H'), ('yearRain', 'H'),
    ('dayET', 'H'), ('monthET', 'H'), ('yearET', 'H'),
    ('soilMoist1', 'B'), ('soilMoist2', 'B'), ('soilMoist3', 'B'),
    ('soilMoist4', 'B'), ('leafWet1', 'B'), ('leafWet2', 'B'),
    ('leafWet3', 'B'), ('leafWet4', 'B'), ('insideAlarm', 'B'),
    ('rainAlarm', 'B'), ('outsideAlarm1', 'B'), ('outsideAlarm2', 'B'),
    ('extraAlarm1', 'B'), ('extraAlarm2', 'B'), ('extraAlarm3', 'B'),
    ('extraAlarm4', 'B'), ('extraAlarm5', 'B'), ('extraAlarm6', 'B'),
    ('extraAlarm7', 'B'), ('extraAlarm8', 'B'), ('soilLeafAlarm1', 'B'),
    ('soilLeafAlarm2', 'B'), ('soilLeafAlarm3', 'B'), ('soilLeafAlarm4', 'B'),
    ('txBatteryStatus', 'B'), ('consBatteryVoltage', 'H'), ('forecastIcon', 'B'),
    ('forecastRule', 'B'), ('sunrise', 'H'), ('sunset', 'H')
]

loop2_schema = [
    ('loop', '3s'), ('trendIcon', 'b'), ('packet_type', 'B'),
    ('_unused', 'H'), ('barometer', 'H'), ('inTemp', 'h'),
    ('inHumidity', 'B'), ('outTemp', 'h'), ('windSpeed', 'B'),
    ('_unused', 'B'), ('windDir', 'H'), ('windSpeed10', 'H'),
    ('windSpeed2', 'H'), ('windGust10', 'H'), ('windGustDir10', 'H'),
    ('_unused', 'H'), ('_unused', 'H'), ('dewpoint', 'h'),
    ('_unused', 'B'), ('outHumidity', 'B'), ('_unused', 'B'),
    ('heatindex', 'h'), ('windchill', 'h'), ('THSW', 'h'),
    ('rainRate', 'H'), ('UV', 'B'), ('radiation', 'H'),
    ('stormRain', 'H'), ('stormStart', 'H'), ('dayRain', 'H'),
    ('rain15', 'H'), ('hourRain', 'H'), ('dayET', 'H'),
    ('rain24', 'H'), ('bar_reduction', 'B'), ('bar_offset', 'h'),
    ('bar_calibration', 'h'), ('pressure_raw', 'H'), ('pressure', 'H'),
    ('altimeter', 'H'), ('_unused', 'B'), ('_unused', 'B'),
    ('_unused_graph', 'B'), ('_unused_graph', 'B'), ('_unused_graph', 'B'),
    ('_unused_graph', 'B'), ('_unused_graph', 'B'), ('_unused_graph', 'B'),
    ('_unused_graph', 'B'), ('_unused_graph', 'B'), ('_unused_graph', 'B'),
    ('_unused_graph', 'B'), ('_unused', 'H'), ('_unused', 'H'),
    ('_unused', 'H'), ('_unused', 'H'), ('_unused', 'H'),
    ('_unused', 'H')
]

# Extract the types and struct.Struct formats for the two types of LOOP packets
loop1_types, loop1_code = list(zip(*loop1_schema))
loop1_struct = struct.Struct('<' + ''.join(loop1_code))
loop2_types, loop2_code = list(zip(*loop2_schema))
loop2_struct = struct.Struct('<' + ''.join(loop2_code))

# ===============================================================================
#                              archive packet
# ===============================================================================

rec_A_schema = [
    ('date_stamp', 'H'), ('time_stamp', 'H'), ('outTemp', 'h'),
    ('highOutTemp', 'h'), ('lowOutTemp', 'h'), ('rain', 'H'),
    ('rainRate', 'H'), ('barometer', 'H'), ('radiation', 'H'),
    ('wind_samples', 'H'), ('inTemp', 'h'), ('inHumidity', 'B'),
    ('outHumidity', 'B'), ('windSpeed', 'B'), ('windGust', 'B'),
    ('windGustDir', 'B'), ('windDir', 'B'), ('UV', 'B'),
    ('ET', 'B'), ('invalid_data', 'B'), ('soilMoist1', 'B'),
    ('soilMoist2', 'B'), ('soilMoist3', 'B'), ('soilMoist4', 'B'),
    ('soilTemp1', 'B'), ('soilTemp2', 'B'), ('soilTemp3', 'B'),
    ('soilTemp4', 'B'), ('leafWet1', 'B'), ('leafWet2', 'B'),
    ('leafWet3', 'B'), ('leafWet4', 'B'), ('extraTemp1', 'B'),
    ('extraTemp2', 'B'), ('extraHumid1', 'B'), ('extraHumid2', 'B'),
    ('readClosed', 'H'), ('readOpened', 'H'), ('unused', 'B')
]

rec_B_schema = [
    ('date_stamp', 'H'), ('time_stamp', 'H'), ('outTemp', 'h'),
    ('highOutTemp', 'h'), ('lowOutTemp', 'h'), ('rain', 'H'),
    ('rainRate', 'H'), ('barometer', 'H'), ('radiation', 'H'),
    ('wind_samples', 'H'), ('inTemp', 'h'), ('inHumidity', 'B'),
    ('outHumidity', 'B'), ('windSpeed', 'B'), ('windGust', 'B'),
    ('windGustDir', 'B'), ('windDir', 'B'), ('UV', 'B'),
    ('ET', 'B'), ('highRadiation', 'H'), ('highUV', 'B'),
    ('forecastRule', 'B'), ('leafTemp1', 'B'), ('leafTemp2', 'B'),
    ('leafWet1', 'B'), ('leafWet2', 'B'), ('soilTemp1', 'B'),
    ('soilTemp2', 'B'), ('soilTemp3', 'B'), ('soilTemp4', 'B'),
    ('download_record_type', 'B'), ('extraHumid1', 'B'), ('extraHumid2', 'B'),
    ('extraTemp1', 'B'), ('extraTemp2', 'B'), ('extraTemp3', 'B'),
    ('soilMoist1', 'B'), ('soilMoist2', 'B'), ('soilMoist3', 'B'),
    ('soilMoist4', 'B')
]

# Extract the types and struct.Struct formats for the two types of archive packets:
rec_types_A, fmt_A = list(zip(*rec_A_schema))
rec_types_B, fmt_B = list(zip(*rec_B_schema))
rec_A_struct = struct.Struct('<' + ''.join(fmt_A))
rec_B_struct = struct.Struct('<' + ''.join(fmt_B))

# These are extra sensors, not found on the Vues.
extra_sensors = {
    'leafTemp1', 'leafTemp2', 'leafWet1', 'leafWet2',
    'soilTemp1', 'soilTemp2', 'soilTemp3', 'soilTemp4',
    'extraHumid1', 'extraHumid2', 'extraTemp1', 'extraTemp2', 'extraTemp3',
    'soilMoist1', 'soilMoist2', 'soildMoist3', 'soilMoist4'
}


def _rxcheck(model_type, interval, iss_id, number_of_wind_samples):
    """Gives an estimate of the fraction of packets received.

    Ref: Vantage Serial Protocol doc, V2.1.0, released 25-Jan-05; p42"""
    # The formula for the expected # of packets varies with model number.
    if model_type == 1:
        _expected_packets = float(interval * 60) / (2.5 + (iss_id - 1) / 16.0) - \
                            float(interval * 60) / (50.0 + (iss_id - 1) * 1.25)
    elif model_type == 2:
        _expected_packets = 960.0 * interval / float(41 + iss_id - 1)
    else:
        return None
    _frac = number_of_wind_samples * 100.0 / _expected_packets
    if _frac > 100.0:
        _frac = 100.0
    return _frac


# ===============================================================================
#                      Decoding routines
# ===============================================================================


def _archive_datetime(datestamp, timestamp):
    """Returns the epoch time of the archive packet."""
    try:
        # Construct a time tuple from Davis time. Unfortunately, as timestamps come
        # off the Vantage logger, there is no way of telling whether or not DST is
        # in effect. So, have the operating system guess by using a '-1' in the last
        # position of the time tuple. It's the best we can do...
        time_tuple = (((0xfe00 & datestamp) >> 9) + 2000,  # year
                      (0x01e0 & datestamp) >> 5,  # month
                      (0x001f & datestamp),  # day
                      timestamp // 100,  # hour
                      timestamp % 100,  # minute
                      0,  # second
                      0, 0, -1)  # have OS guess DST
        # Convert to epoch time:
        ts = int(time.mktime(time_tuple))
    except (OverflowError, ValueError, TypeError):
        ts = None
    return ts


def _loop_date(p, k):
    """Returns the epoch time stamp of a time encoded in the LOOP packet,
    which, for some reason, uses a different encoding scheme than the archive packet.
    Also, the Davis documentation isn't clear whether "bit 0" refers to the least-significant
    bit, or the most-significant bit. I'm assuming the former, which is the usual
    in little-endian machines."""
    v = p[k]
    if v == 0xffff:
        return None
    time_tuple = ((0x007f & v) + 2000,  # year
                  (0xf000 & v) >> 12,  # month
                  (0x0f80 & v) >> 7,  # day
                  0, 0, 0,  # h, m, s
                  0, 0, -1)
    # Convert to epoch time:
    try:
        ts = int(time.mktime(time_tuple))
    except (OverflowError, ValueError):
        ts = None
    return ts


def _decode_rain(p, k):
    if p['bucket_type'] == 0:
        # 0.01 inch bucket
        return p[k] / 100.0
    elif p['bucket_type'] == 1:
        # 0.2 mm bucket
        return p[k] * 0.0078740157
    elif p['bucket_type'] == 2:
        # 0.1 mm bucket
        return p[k] * 0.00393700787
    else:
        log.warning("Unknown bucket type $s" % p['bucket_type'])


def _decode_windSpeed_H(p, k):
    """Decode 10-min average wind speed. It is encoded slightly
    differently between type 0 and type 1 LOOP packets."""
    if p['packet_type'] == 0:
        return float(p[k]) if p[k] != 0xff else None
    elif p['packet_type'] == 1:
        return float(p[k]) / 10.0 if p[k] != 0xffff else None
    else:
        log.warning("Unknown LOOP packet type %s" % p['packet_type'])


# This dictionary maps a type key to a function. The function should be able to
# decode a sensor value held in the LOOP packet in the internal, Davis form into US
# units and return it.
# NB: 5/28/2022. In a private email with Davis support, they say that leafWet3 and leafWet4 should
# always be ignored. They are not supported.
_loop_map = {
    'altimeter': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'bar_calibration': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'bar_offset': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'bar_reduction': lambda p, k: p[k],
    'barometer': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'consBatteryVoltage': lambda p, k: float((p[k] * 300) >> 9) / 100.0,
    'dayET': lambda p, k: float(p[k]) / 1000.0,
    'dayRain': _decode_rain,
    'dewpoint': lambda p, k: float(p[k]) if p[k] & 0xff != 0xff else None,
    'extraAlarm1': lambda p, k: p[k],
    'extraAlarm2': lambda p, k: p[k],
    'extraAlarm3': lambda p, k: p[k],
    'extraAlarm4': lambda p, k: p[k],
    'extraAlarm5': lambda p, k: p[k],
    'extraAlarm6': lambda p, k: p[k],
    'extraAlarm7': lambda p, k: p[k],
    'extraAlarm8': lambda p, k: p[k],
    'extraHumid1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid3': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid4': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid5': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid6': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid7': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp3': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp4': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp5': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp6': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp7': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'forecastIcon': lambda p, k: p[k],
    'forecastRule': lambda p, k: p[k],
    'heatindex': lambda p, k: float(p[k]) if p[k] & 0xff != 0xff else None,
    'hourRain': _decode_rain,
    'inHumidity': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'insideAlarm': lambda p, k: p[k],
    'inTemp': lambda p, k: float(p[k]) / 10.0 if p[k] != 0x7fff else None,
    'leafTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafTemp3': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafTemp4': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafWet1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'leafWet2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'leafWet3': lambda p, k: None,  # Vantage supports only 2 leaf wetness sensors
    'leafWet4': lambda p, k: None,
    'monthET': lambda p, k: float(p[k]) / 100.0,
    'monthRain': _decode_rain,
    'outHumidity': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'outsideAlarm1': lambda p, k: p[k],
    'outsideAlarm2': lambda p, k: p[k],
    'outTemp': lambda p, k: float(p[k]) / 10.0 if p[k] != 0x7fff else None,
    'pressure': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'pressure_raw': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'radiation': lambda p, k: float(p[k]) if p[k] != 0x7fff else None,
    'rain15': _decode_rain,
    'rain24': _decode_rain,
    'rainAlarm': lambda p, k: p[k],
    'rainRate': _decode_rain,
    'soilLeafAlarm1': lambda p, k: p[k],
    'soilLeafAlarm2': lambda p, k: p[k],
    'soilLeafAlarm3': lambda p, k: p[k],
    'soilLeafAlarm4': lambda p, k: p[k],
    'soilMoist1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist3': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist4': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp3': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp4': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'stormRain': _decode_rain,
    'stormStart': _loop_date,
    'sunrise': lambda p, k: 3600 * (p[k] // 100) + 60 * (p[k] % 100),
    'sunset': lambda p, k: 3600 * (p[k] // 100) + 60 * (p[k] % 100),
    'THSW': lambda p, k: float(p[k]) if p[k] & 0xff != 0xff else None,
    'trendIcon': lambda p, k: p[k],
    'txBatteryStatus': lambda p, k: int(p[k]),
    'UV': lambda p, k: float(p[k]) / 10.0 if p[k] != 0xff else None,
    'windchill': lambda p, k: float(p[k]) if p[k] & 0xff != 0xff else None,
    'windDir': lambda p, k: (float(p[k]) if p[k] != 360 else 0) if p[k] and p[k] != 0x7fff else None,
    'windGust10': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'windGustDir10': lambda p, k: (float(p[k]) if p[k] != 360 else 0) if p[k] and p[k] != 0x7fff else None,
    'windSpeed': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'windSpeed10': _decode_windSpeed_H,
    'windSpeed2': _decode_windSpeed_H,
    'yearET': lambda p, k: float(p[k]) / 100.0,
    'yearRain': _decode_rain,
}

# This dictionary maps a type key to a function. The function should be able to
# decode a sensor value held in the archive packet in the internal, Davis form into US
# units and return it.
_archive_map = {
    'barometer': lambda p, k: float(p[k]) / 1000.0 if p[k] else None,
    'ET': lambda p, k: float(p[k]) / 1000.0,
    'extraHumid1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraHumid2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'extraTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'extraTemp3': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'forecastRule': lambda p, k: p[k] if p[k] != 193 else None,
    'highOutTemp': lambda p, k: float(p[k] / 10.0) if p[k] != -32768 else None,
    'highRadiation': lambda p, k: float(p[k]) if p[k] != 0x7fff else None,
    'highUV': lambda p, k: float(p[k]) / 10.0 if p[k] != 0xff else None,
    'inHumidity': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'inTemp': lambda p, k: float(p[k]) / 10.0 if p[k] != 0x7fff else None,
    'leafTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'leafWet1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'leafWet2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'leafWet3': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'leafWet4': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'lowOutTemp': lambda p, k: float(p[k]) / 10.0 if p[k] != 0x7fff else None,
    'outHumidity': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'outTemp': lambda p, k: float(p[k]) / 10.0 if p[k] != 0x7fff else None,
    'radiation': lambda p, k: float(p[k]) if p[k] != 0x7fff else None,
    'rain': _decode_rain,
    'rainRate': _decode_rain,
    'readClosed': lambda p, k: p[k],
    'readOpened': lambda p, k: p[k],
    'soilMoist1': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist2': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist3': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilMoist4': lambda p, k: float(p[k]) if p[k] != 0xff else None,
    'soilTemp1': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp2': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp3': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'soilTemp4': lambda p, k: float(p[k] - 90) if p[k] != 0xff else None,
    'UV': lambda p, k: float(p[k]) / 10.0 if p[k] != 0xff else None,
    'wind_samples': lambda p, k: float(p[k]) if p[k] else None,
    'windDir': lambda p, k: float(p[k]) * 22.5 if p[k] != 0xff else None,
    'windGust': lambda p, k: float(p[k]),
    'windGustDir': lambda p, k: float(p[k]) * 22.5 if p[k] != 0xff else None,
    'windSpeed': lambda p, k: float(p[k]) if p[k] != 0xff else None,
}
