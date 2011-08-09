import serial
import threading
import sys
import codecs 
import time
import glob
import time

#From the wsnserver project
import Controller

#Better Serial access with Python
from serial import Serial
class EnhancedSerial(Serial):
    def __init__(self, *args, **kwargs):
        #ensure that a reasonable timeout is set
        timeout = kwargs.get('timeout',0.1)
        if timeout < 0.01: timeout = 0.1
        kwargs['timeout'] = timeout
        Serial.__init__(self, *args, **kwargs)
        self.buf = ''
        
    def readline(self, maxsize=None, timeout=1):
        """maxsize is ignored, timeout in seconds is the max time that is way for a complete line"""
        tries = 0
        while 1:
            self.buf += self.read(512)
            pos = self.buf.find('\n')
            if pos >= 0:
                line, self.buf = self.buf[:pos+1], self.buf[pos+1:]
                return line
            tries += 1
            if tries * self.timeout > timeout:
                break
        line, self.buf = self.buf, ''
        return line

class SerialReader:
    def __init__(self, verbose=True):
	self.controllerId = ''
	self.verbose = verbose

        self.serial = EnhancedSerial(1)
        self.serial.port     = self.find_port()
        self.serial.baudrate = 38400

        try:
            self.serial.open()
        except serial.SerialException, e:
            sys.stderr.write("Could not open serial port %s: %s\n" % (self.serial.portstr, e))
            sys.exit(1)

	#Read buffer first time to flush
	i = 0;
	while i < 10:
		self.reader()
		i = i + 1

	self.controller = Controller.Controller()
        
    def shortcut(self):
	#Get ID from WSN
	if len(self.controllerId) == 0:
		self.write("+WPANID\r")
		time.sleep(1)
		self.controllerId = self.reader()
		self.controller.saveDevice(self.controllerId)
		return

	#receive data
	outdata = self.reader()
	if len(outdata) > 0:
		self.controller.saveDataAction(self.controllerId, outdata)
	#send data
	indata = self.controller.readCMDAction(self.controllerId);
	if indata:
		self.write(indata)
		sleep(1)
		

    def find_port(self):
        port = glob.glob('/dev/ttyUSB*')
        if len(port) != 1:
            print "Only one USB-FDDI adapter required - no more or less"
            sys.exit(1)
        else:
            return port[0]
        
    def reader(self):
	data = ''
	#while self.serial.inWaiting() > 0:
	#	data += self.serial.read(1)
	data = self.serial.readline()
	if self.verbose and len(data) > 0:
		sys.stdout.write("input:" + data)
		sys.stdout.flush()
	return data.strip()
	
    def write(self,data):
	self.serial.write(data)                 # get a bunch of bytes and send them
        # Verbose mode prints everthing to console
        if self.verbose:
       		sys.stdout.write("output:" + data)
                sys.stdout.flush()

if __name__ == '__main__':
# connect to serial port and do some test if not run as module

#Commandline parsing
    import optparse

    parser = optparse.OptionParser(
     usage = "%prog [options]",
     description = "Wireless Sensor Network to TCP bridge with puffering",
     epilog = """\
        NOTE: no security measures are implemented. Anyone can remotely connect
        to this service over the network.

        Only one connection at once is supported. When the connection is terminated
        it waits for the next connect.
        """)

    parser.add_option("-v",
        dest = "verbose",
        action = "store_true",
        help = "write all serial in- and output to the console",
        default = False
    )

    (options, args) = parser.parse_args()

    
    s = SerialReader(options.verbose)

    while True:
        try:
            s.shortcut()
        except KeyboardInterrupt:
            break


    sys.stderr.write('\n--- exit ---\n')
