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

        # Station 5
        self.switchJourney1 = None
        self.switchJourney2 = None
        self.switchJourney3 = None
        self.switchJourney4 = None
        self.switchJourney5 = None
        self.switchJourney6 = None
        self.switchJourney7 = None
        self.motor1State = None
        self.motor2State = None
        self.motor3State = None
        self.motor4State = None
        self.motor5State = None
        self.servo1degree = None
        self.servo2degree = None
        self.stationState = None

        self._serial = serial.Serial(self._serialport, self._baudrate)

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
        # if data.find("MT;0;") >= 0:
        #     retry = 3
        #     while retry > 0:
        #         self._serial.write(str.encode(data + '!', 'utf-8'))
        #         time.sleep(0.3)
        #         retry -= 1
        # else:
        self._serial.write(str.encode(data + '!', 'utf-8'))

    def inWaiting(self):
        self._serial.inWaiting()

    def flushInput(self):
        self._serial.flushInput()

    def flushOutput(self):
        self._serial.flushOutput()

    def setNodesStation05(self, switchJourney1, switchJourney2, switchJourney3, switchJourney4, switchJourney5, switchJourney6, switchJourney7, motor1State, motor2State, motor3State, motor4State, motor5State, servo1degree, servo2degree, stationState):
        self.switchJourney1 = switchJourney1
        self.switchJourney2 = switchJourney2
        self.switchJourney3 = switchJourney3
        self.switchJourney4 = switchJourney4
        self.switchJourney5 = switchJourney5
        self.switchJourney6 = switchJourney6
        self.switchJourney7 = switchJourney7
        self.motor1State = motor1State
        self.motor2State = motor2State
        self.motor3State = motor3State
        self.motor4State = motor4State
        self.motor5State = motor5State
        self.servo1degree = servo1degree
        self.servo2degree = servo2degree
        self.stationState = stationState

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
            if v.find("MT;0;RUN") >= 0:
                if not self.motor1State is None:
                    self.motor1State.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;0;STOP") >= 0:
                if not self.motor1State is None:
                    self.motor1State.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("MT;1;RUN") >= 0:
                if not self.motor2State is None:
                    self.motor2State.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;1;STOP") >= 0:
                if not self.motor2State is None:
                    self.motor2State.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("MT;2;RUN") >= 0:
                if not self.motor3State is None:
                    self.motor3State.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;2;STOP") >= 0:
                if not self.motor3State is None:
                    self.motor3State.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("MT;3;RUN") >= 0:
                if not self.motor4State is None:
                    self.motor4State.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;3;STOP") >= 0:
                if not self.motor4State is None:
                    self.motor4State.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("MT;4;RUN") >= 0:
                if not self.motor5State is None:
                    self.motor5State.set_value("RUNNING")
                    self.write("#OK")
            elif v.find("MT;4;STOP") >= 0:
                if not self.motor5State is None:
                    self.motor5State.set_value("STOPPING")
                    self.write("#OK")
            elif v.find("SS;0;0") >= 0:
                if not self.switchJourney1 is None:
                    self.switchJourney1.set_value(True)
                    self.write("#OK")
            elif v.find("SS;0;1") >= 0:
                if not self.switchJourney1 is None:
                    self.switchJourney1.set_value(False)
                    self.write("#OK")
            elif v.find("SS;1;0") >= 0:
                if not self.switchJourney2 is None:
                    self.switchJourney2.set_value(True)
                    self.write("#OK")
            elif v.find("SS;1;1") >= 0:
                if not self.switchJourney2 is None:
                    self.switchJourney2.set_value(False)      
                    self.write("#OK")
            elif v.find("SS;2;0") >= 0:
                if not self.switchJourney3 is None:
                    self.switchJourney3.set_value(True)
                    self.write("#OK")
            elif v.find("SS;2;1") >= 0:
                if not self.switchJourney3 is None:
                    self.switchJourney3.set_value(False)      
                    self.write("#OK")
            elif v.find("SS;3;0") >= 0:
                if not self.switchJourney4 is None:
                    self.switchJourney4.set_value(True)
                    self.write("#OK")
            elif v.find("SS;3;1") >= 0:
                if not self.switchJourney4 is None:
                    self.switchJourney4.set_value(False)      
                    self.write("#OK")
            elif v.find("SS;4;0") >= 0:
                if not self.switchJourney5 is None:
                    self.switchJourney5.set_value(True)
                    self.write("#OK")
            elif v.find("SS;4;1") >= 0:
                if not self.switchJourney5 is None:
                    self.switchJourney5.set_value(False)      
                    self.write("#OK")
            elif v.find("SS;5;0") >= 0:
                if not self.switchJourney6 is None:
                    self.switchJourney6.set_value(True)
                    self.write("#OK")
            elif v.find("SS;5;1") >= 0:
                if not self.switchJourney6 is None:
                    self.switchJourney6.set_value(False)      
                    self.write("#OK")
            elif v.find("SS;6;0") >= 0:
                if not self.switchJourney7 is None:
                    self.switchJourney7.set_value(True)
                    self.write("#OK")
            elif v.find("SS;6;1") >= 0:
                if not self.switchJourney7 is None:
                    self.switchJourney7.set_value(False)      
                    self.write("#OK")
            elif v.find("SV;0") >= 0:
                if not self.servo1degree is None:
                    self.servo1degree.set_value(v.split(";")[3])
                    self.write("#OK")
            elif v.find("SV;1") >= 0:
                if not self.servo2degree is None:
                    self.servo2degree.set_value(v.split(";")[3])
                    self.write("#OK")
            elif v.find("ST;START") >= 0:
                if not self.stationState is None:
                    self.stationState.set_value("RUN")
                    self.write("#OK")
            elif v.find("ST;PAUSE") >= 0:
                if not self.stationState is None:
                    self.stationState.set_value("STOP")
                    self.write("#OK")
            v = None
        
        self.close()