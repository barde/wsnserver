import serial
import threading
import sys
import codecs
import time

class SerialReader:
    def __init__(self,serial_instance,verbose=True):
        self.serial = serial_instance
	self.verbose = verbose
        
    def shortcut(self):
        """connect the serial port to the TCP port by copying everything
           from one side to the other"""
        self.alive = True
        self.thread_read = threading.Thread(target=self.reader)
        self.thread_read.setDaemon(True)
        self.thread_read.setName('socket reader')
        self.thread_read.start()
        

    def reader(self):
        """loop forever and copy serial->command i/o"""
        while self.alive:
            data = self.serial.read(1)              # read one, blocking
            n = self.serial.inWaiting()             # look if there is more
            if n:
                data = data + self.serial.read(n)   # and get as much as possible
            if data:
                # verbosity for copying the serial data to the console
                if self.verbose:
                    sys.stdout.write(codecs.escape_encode(data)[0])
                    sys.stdout.flush()
                '''                    
                # send the data to the listing component
                self._write_lock.acquire()                    
                try:
                    self.socket.sendall(data)           # send it over TCP
                finally:
                    self._write_lock.release()
                '''
        self.alive = False


    def writer(self):
        """loop forever and copy socket->serial"""
        while self.alive:
            #Read data from reading component
            #data = self.socket.recv(1024)
            if not data:
                break
            self.serial.write(data)                 # get a bunch of bytes and send them
            # the spy shows what's on the serial port, so log it after converting newlines
            if self.verbose:
                sys.stdout.write(codecs.escape_encode(data)[0])
                sys.stdout.flush()
        self.alive = False
        self.thread_read.join()

    def stop(self):
        """Stop copying"""
        if self.alive:
            self.alive = False
            self.thread_read.join()

    

#if __name__ == '__main__':
# connect to serial port

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

parser.add_option("--v",
        dest = "verbose",
        action = "store_true",
        help = "write all serial in- and output to the console",
        default = False
    )

(options, args) = parser.parse_args()

ser = serial.Serial()
ser.port     = "/dev/ttyUSB1"
ser.baudrate = 38400


try:
    ser.open()
except serial.SerialException, e:
    sys.stderr.write("Could not open serial port %s: %s\n" % (ser.portstr, e))
    sys.exit(1)
    
    
while True:
    try:
        s = SerialReader(ser,options.verbose)
        s.shortcut()
        time.sleep(1)
    except KeyboardInterrupt:
        break

sys.stderr.write('\n--- exit ---\n')
    
