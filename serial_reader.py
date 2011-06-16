import serial
import threading
import sys
import codecs
import time

class SerialReader:
    def __init__(self,serial_instance):
        self.serial = serial_instance
        
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
                    # the spy shows what's on the serial port, so log it before converting newlines
                    if True:
                        sys.stdout.write(codecs.escape_encode(data)[0])
                        sys.stdout.flush()
                    '''                    
                    if self.ser_newline and self.net_newline:
                        # do the newline conversion
                        # XXX fails for CR+LF in input when it is cut in half at the begin or end of the string
                        data = net_newline.join(data.split(ser_newline))
                    # escape outgoing data when needed (Telnet IAC (0xff) character)
                    self._write_lock.acquire()                    
                    try:
                        self.socket.sendall(data)           # send it over TCP
                    finally:
                        self._write_lock.release()
                        '''
	self.alive = False
	

#if __name__ == '__main__':
# connect to serial port
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
        s = SerialReader(ser)
        s.shortcut()
	time.sleep(1)
    except KeyboardInterrupt:
        break

sys.stderr.write('\n--- exit ---\n')
    
