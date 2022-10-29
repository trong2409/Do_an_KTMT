import serial
from threading import Thread
import time, re

class SerialCommunication(Thread):
    def __init__(self, serialport, baudrate=None, bytesize=None, parity=None, stopbits=None, readtimeout=None, writetimeout=None, xonxoff=None, rtscts=None, dsrdtr=None):
        Thread.__init__(self)
        self._stopev = False

        if serialport is not None:
            self._serialport = serialport

        if baudrate is None:
            self._baudrate = 115200
        else:
            self._baudrate = baudrate

        if bytesize is None:
            self._bytesize = serial.EIGHTBITS
        else:
            self._bytesize = bytesize

        if parity is None:
            self._parity = serial.PARITY_NONE
        else:
            self._parity = parity

        if stopbits is None:
            self._stopbits = serial.STOPBITS_ONE
        else:
            self._stopbits = stopbits

        if readtimeout is None:
            self._readtimeout = 10
        else:
            self._readtimeout = readtimeout

        if writetimeout is None:
            self._writetimeout = 0
        else:
            self._writetimeout = writetimeout

        if xonxoff is None:
            self._xonxoff = False
        else:
            self._xonxoff = xonxoff

        if rtscts is None:
            self._rtscts = False
        else:
            self._rtscts = rtscts

        if dsrdtr is None:
            self._dsrdtr = False
        else:
            self._dsrdtr = dsrdtr

        # Station 7
        self.sensor = None

        self._serial = serial.Serial(self._serialport, self._baudrate)
        self._value = 0

    @property
    def serialport(self):
        return self._serialport

    @property
    def baudrate(self):
        return self._baudrate

    @property
    def bytesize(self):
        return self._bytesize

    @property
    def parity(self):
        return self._parity
        
    @property
    def stopbits(self):
        return self._stopbits

    @property
    def readtimeout(self):
        return self._readtimeout

    @property
    def writetimeout(self):
        return self._writetimeout

    @property
    def xonxoff(self):
        return self._xonxoff

    @property
    def rtscts(self):
        return self._rtscts

    @property
    def dsrdtr(self):
        return self._dsrdtr

    def getValue(self):
        return self._value

    def readline(self):
        return self._serial.readline()

    def read(self):
        return self._serial.read()

    def readLength(self, length):
        return self._serial.read(length)

    def open(self):
        return self._serial.open()

    def close(self):
        return self._serial.close()
    
    def isOpen(self):
        return self._serial.isOpen()

    def stop(self):
        self._stopev = True

    def write(self, data):
        self._serial.write(str.encode(data + '!', 'utf-8'))

    def inWaiting(self):
        self._serial.inWaiting()

    def flushInput(self):
        self._serial.flushInput()

    def flushOutput(self):
        self._serial.flushOutput()

    def setNodesStation07(self, sensor, motorState):
        self.sensor = sensor
        self.motorState = motorState

    def doRead(self,term):
        matcher = re.compile(term)
        tic = time.time()
        buff = self._serial.read(1)
        while ((time.time() - tic) < self._readtimeout) and (not matcher.search(buff)):
            buff += self._serial.read(1)
        return buff[:len(buff)-1]

    def run(self):
        try:
            self.open()
        except Exception:
            pass 
        
        self._serial.flushInput()
        self._serial.flushOutput()

        while not self._stopev:
            v = str(self.doRead(b'!'), 'utf-8')
            # self._value = v
            if v.find("MT;0;RUN") >= 0 or v.find("ST")  >= 0:
                if not self.motorState is None:
                    self.motorState.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;0;STOP") >= 0  or v.find("OP")  >= 0:
                if not self.motorState is None:
                    self.motorState.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("SS;0;0") >= 0:
                if not self.sensor is None:
                    self.sensor.set_value(True)
                    self.write("#OK")
            elif v.find("SS;0;1") >= 0:
                if not self.sensor is None:
                    self.sensor.set_value(False)
                    self.write("#OK")
            v = None
        
        self.close()