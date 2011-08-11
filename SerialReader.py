#!/usr/bin/env python
#
#wsnserver - the serial hardware component
#
#written 7.2011 by Bartholomaeus Dedersen
##http://selbstapotheose.de
#
#for
#
#FH Kiel
#Prof. Dispert
#Master IT
#Ubiquitous Computing
#Project for a RESTful http bridge for Wireless Sensor Nodes
#
#Purpose of this file:
#
#Mainly work by me except the first class. I included two objects.
#
#The first one, EnchacedSerial, is from the 
#repositories of PySerial. It is under the Python-License.
#
#
#
#The second class is about the real communication.
#Use the source, Luke.
 #
  #
   ############

import serial
import threading
import sys
import codecs 
import time
import glob
import time

#Refactored Singleton
import LazyData

#From the wsnserver project - the controller for the database
#and sexy http-interface
import Controller

#Better Serial access with Python - taken
#from PySerial's cvs

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




#Prepare for the most ingenious
#and sophisticated Serial reader you
#ever read. Full of Adapter design patterns,
#a hell of a facade and the most most useless all-seeing,
#omnipotent servant called "servant" - all made with loosest coupling
#you can ever imagine.
#It is the first python code I ever wrote in my life.

#tl;dr: this Object defines an interface for accessing WSN or if used
#as an executable it uses anti-threads to handle all hardware-stuff

class SerialReader:

    def __init__(self, verbose, aggressive_mode, wsnport, command, baud):
        #Our buffer
        lazyData = LazyData.LazyData()
        __data = lazyData.content
    
        #Save the ID of the controller WSN here
        self.controllerId = ''
    
        #controller object is instanced here
        self.controller = Controller.Controller()

        #Tell me more on output
        self.verbose = verbose

        #Save the port of the WSN if there was any
        self.wsnport = wsnport

        #One line of command was passed - please expl0it and inj3ct me!
        __data = command

        #Ask for more speed and less reliability?
        self.aggressive_mode = aggressive_mode

        #configuration for the serial port
        #which is given by an FTDI usb converter
        if self.aggressive_mode:
            self.serial = serial.Serial()
        else:
            self.serial = EnhancedSerial(timeout=1)

        #auto detection of WSN connection works only for FTDI usb->serial
        #with linux
        if not self.wsnport:
            self.wsnport     = self.find_port()


        #Either the auto find or via console parametre
        print "Port: " + self.wsnport
        self.serial.port     = self.wsnport


        #Use them if you need'em
        #self.serial.parity=serial.PARITY_ODD,
        #self.serial.stopbits=serial.STOPBITS_TWO,
        #self.serial.bytesize=serial.SEVENBITS

        
        #change Baudrate on command line or take our variable - Basta!
        if baud:
            self.serial.baudrate = baud
        else:
            self.serial.baudrate = 38400


        try:
            self.serial.open()
        except serial.SerialException, e:
            sys.stderr.write("Could not open serial port %s: %s\n" % (self.serial.portstr, e))
            sys.exit(1)

        """
        #Read buffer first 10 times to flush
        i = 0;
        while i < 10:
            self.reader()
            i = i + 1
        """


            
    #servant for the object if ran as executable
    def servant(self):
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
        #sometimes there is nothing to write. We are fine with it.
        if indata:
            self.write(indata)
            sleep(1)
            return
        #but sometimes there will be more than one command so we
        #just wait for a new round.
        #12.5 Hertz on our 3Ghz Celeron 
        #with 420 MB RAM(Rest to 512 got killed by age)!

        #Wait, we have sometimes data to write in one cycle!
        #But please only one write so everytime a return is 
        #adviced
        if len(data.content) != 0:
            self.write(data.content)
            data.content = ""
            return
            

        

    #FTDI-USB gets connected by /dev/ttyUSB[0-9]
    #Serial gets connected by /dev/ttyS[0-9]
    #Windows and Mac --> http://pyserial.sourceforge.net/
    def find_port(self):
        port = glob.glob('/dev/ttyUSB*')
        if len(port) != 1:
            sys.stderr.write("Only _one_ USB-FTDI adapter required - no more or less")
            sys.exit(1)
        else:
            return port[0]


        
    def reader(self):
        data = ''

        if self.aggressive_mode:
            while self.serial.inWaiting() > 0:
                data += self.serial.read(1)
        else:
            data = self.serial.readline()

            # Verbose mode prints everthing to console
        if self.verbose and len(data) > 0:
            sys.stdout.write("rx:" + data)
            sys.stdout.flush()
        return data.strip()


    
    def write(self,data):
        self.serial.write(data)                 # get a bunch of bytes and send them
        # Verbose mode prints everthing to console
        if self.verbose:
           sys.stdout.write("tx:" + data)
           sys.stdout.flush()





#Bienvenue and welcome to our small main()
if __name__ == '__main__':


#Commandline parsing
    import optparse

    parser = optparse.OptionParser(
     usage = "%prog [options]",
     description = "Hardware component of wsnserver",
     epilog = """ Run me stand alone and I will serve the Serial Hardware WSN
        for you. Maybe I will need some frontend like a http-server but 
        look at the controller object Controller.py!
        
        This file contains also a usable interface as an object. For 
        modification and interface use the source code.
            """)

    parser.add_option("-v", "--verbose",
        dest = "verbose",
        action = "store_true",
        help = "write all serial in- and output to the console",
        default = False)

    parser.add_option("-a", "--aggressive",
    dest = "aggressive_mode",
    action = "store_true",
    help = "do not wait for serial data new line and rely on fast WSN",
    default = False)

    parser.add_option("-p", "--port", 
    dest="port",
    help="use PORT for communication and skip auto detection", 
    metavar="PORT")

    parser.add_option("-i", "--interactive",
    dest="interactive",
    help="use %prog as terminal emulator",
    default = False)

    parser.add_option("-c", "--command",
        action="store",
        type="string",
        help = "pass COMMAND as input to the WSN",
    metavar="COMMAND",
        dest="command")


    parser.add_option("-b",
    action="store",
    type="string",
    help="set baudrate to BAUD(9600,38400,115200)",
    metavar="BAUD",
    dest="baud")


    #Get our command line parameters
    (options, args) = parser.parse_args()

    #Create one of our objects
    s = SerialReader(options.verbose, 
        options.aggressive_mode,
        options.port,
        options.command,
        options.baud)

    #Enable our buffer
    data = LazyData.LazyData()


    while True:
        try:
            if options.interactive:
                input = raw_input()
                data.content = input
            s.servant()
        except KeyboardInterrupt:
            break
