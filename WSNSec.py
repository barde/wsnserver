#!/usr/bin/env python
# WSNSec
# Secure communication between Wireless Sensor Networks
# with SSL/PKCS#11
#
#written XXX.2011 by Bartholomaeus Dedersen
##http://selbstapotheose.de
#
#for
#
#FH Kiel
#Prof. Dispert
#Master IT
#Ambient Intelligence
#
#TODO:
# - plan, do, check, act
#
#Purpose of this file:
#
#tbd
#
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

class WSNSec:

    def __init__(self):
        self.verbose = True
        if self.verbose:
            print "WSNSec started"
    
    def init_connection(self):
        if self.verbose:
            print "Connection established"
        
    def send_request(self):
        if self.verbose:
            print "stx:" #+ DATA

    
    def receive_data(self):
        if self.verbose:
            print "srx:" #+ DATA
    
    def close_connection(self):
        if self.verbose:
            print "Connection closed"

#Bienvenue and welcome to our small main()
#Sadly, we are just a small main() for testing
#but feel free to expand me to your needs!
if __name__ == '__main__':


#Commandline parsing
    import optparse

    parser = optparse.OptionParser(
     usage = "%prog [options]",
     description = "WSNSec - Security for Wireless Sensor Nodes",
     epilog = """Testing interface for the Security connections for
        Wireless Sensor Nodes.
        
        This file contains also a usable interface as an object. For 
        modification and interface use the source code.
            """)

    parser.add_option("-v", "--verbose",
        dest = "verbose",
        action = "store_true",
        help = "Be more verbose! Default prints only errors.",
        default = False)


    #Get our command line parameters
    (options, args) = parser.parse_args()

s = WSNSec()

s.init_connection()
s.send_request()
s.receive_data()
s.close_connection()
