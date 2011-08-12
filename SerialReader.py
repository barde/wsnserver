#!/usr/bin/env python
# #wsnserver - the serial hardware component
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

#Singleton for sharing data
import LazyData

#More reliable read from console
import EnhancedSerial

#Translator for genericCommand -> [WSN-Dialect]
import Translator

#From the wsnserver project - the controller for the database
#and sexy http-interface
import Controller

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
        

        #Our buffer which is sometimes filled by parametres send by command line
        #or pushed by the database
        self.lazyData = LazyData.LazyData()
    
        if command is not None:
            self.lazyData.content = command
    
        if verbose:
            print "Initial Command: " + self.lazyData.content


        #The translator for generic commands with Renesas WSN
        self.translator = Translator.RenesasTranslator()
    
        #Save the ID of the controller WSN here
        self.controllerId = ''
    
        #controller object is instanced here
        self.controller = Controller.Controller()

        #Tell me more on output
        self.verbose = verbose

        #Save the port of the WSN if there was any
        self.wsnport = wsnport

        #Ask for more speed and less reliability?
        self.aggressive_mode = aggressive_mode

        #configuration for the serial port
        #which is given by an FTDI usb converter
        if self.aggressive_mode:
            self.serial = serial.Serial()
        else:
            self.serial = EnhancedSerial.EnhancedSerial(timeout=0.5)

        #auto detection of WSN connection works only for FTDI usb->serial
        #with linux
        if not self.wsnport:
            self.wsnport     = self.find_port()


        #Either the auto find or via console parametre
        if self.verbose:
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
    #Good for first start or debugging
        i = 0;
        while i < 10:
            self.reader()
            i = i + 1
    """


            
    #servant for the object if ran as executable
    def servant(self):
        #Get ID from WSN
        if len(self.controllerId) == 0:
            self.write(self.translator.tag("GetId"))
            time.sleep(1)
            self.controllerId = self.reader()
            self.controller.saveDevice(self.controllerId)
            return

        #receive data and save it to the database with ID of WSN
        outdata = self.reader()
        if len(outdata) > 0:
            self.controller.saveDataAction(self.controllerId, outdata)

        #Send the data which is waiting
        #But please only one write so everytime a return is 
        #adviced

        if self.lazyData.content:
            self.write(self.lazyData.content)
            self.lazyData.content = ""
            return

        #If there is data waiting in the SQL-Queue -> include it in the 
    #next cycle
        self.lazyData.content = self.controller.readCMDAction(self.controllerId);
        #but sometimes there will be more than one command so we
        #just wait for a new round.
        #12.5 Hertz on our 3Ghz Celeron 
        #with 420 MB RAM(Remaining RAM to 512 MB got killed by age)!

            

        

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



#Small helper function for interactive input/output
#necessary because of threading
def readInput():
    global keyboard_data
    while True:
        keyboard_data = raw_input("? ")


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
    action = "store_true",
    help="use keyboard to send commands to WSN",
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
    lazyData = LazyData.LazyData()

    #Debug purposes
    if options.interactive:
        import thread
        keyboard_data = ""
        thread.start_new_thread(readInput,())


    while True:
        try:
            if options.interactive and len(keyboard_data) != 0:
                lazyData.content = keyboard_data
                keyboard_data = ""
            s.servant()
        except KeyboardInterrupt:
            break

