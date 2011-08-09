import serial
import threading
import sys
import codecs 
import time
import glob

import Controller

class SerialReader:
    def __init__(self, verbose=True):
	self.controllerId = ''
	self.verbose = verbose

        self.serial = serial.Serial()
        self.serial.port     = self.find_port()
        self.serial.baudrate = 38400

        try:
            self.serial.open()
        except serial.SerialException, e:
            sys.stderr.write("Could not open serial port %s: %s\n" % (self.serial.portstr, e))
            sys.exit(1)

	self.controller = Controller.Controller()
        
    def shortcut(self):
	if self.controllerId.count == 0:
		self.write("+WPANID")
		self.controllerId = self.reader()
		return

	#receive data
	outdata = self.reader()
	if len(outdata) > 0:
		self.controller.saveDataAction(self.controllerId, outdata)
	#send data
	indata = self.controller.readCMDAction(self.controllerId);
	if indata:
		self.write(indata)
		

    def find_port(self):
        port = glob.glob('/dev/ttyUSB*')
        if len(port) != 1:
            print "Only one USB-FDDI adapter required - no more or less"
            sys.exit(1)
        else:
            return port[0]
        
    def reader(self):
	data = ''
	while self.serial.inWaiting() > 0:
		data += self.serial.read(1)
	if self.verbose and len(data) > 0:
		sys.stdout.write("input:" + data)
		sys.stdout.flush()
	return data

	


    def write(self,data):
        """loop forever and copy socket->serial"""
        while self.alive:
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
