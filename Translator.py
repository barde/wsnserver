#!/usr/bin/env python
#
#wsnserver - the translation agent
#
#written 2011 by Bartholomaeus Dedersen
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
# This object translates generic commands for WSN
# of different manufacturers.
#
 #
  #
   ############

"""
rx:'+WWSNID'          get WSN ID
rx:'+WCHAN'           get ZigBee channel number
rx:'+WPANID'          get ZigBee PANID
rx:'+WENQ'            send ENQUIRY
rx:'+WLED 1 [ON/OFF]' set LED1 ON/OFF
rx:'+WSENDTEMP'       send Temperature value each minute
rx:'+WNSENDTEMP'      stop sending Temperature value
rx:'help'             get this Command List
"""

#Abstract class
class Translator:
    dictionary = 	{"Whatever":"Something"}

    def tag(self,genericCommand):
        for tag in self.dictionary:
            if tag == genericCommand:
                return self.dictionary[tag]
        return "No dictionary entry found!"
        
#First real dictionary as inherited class
class RenesasTranslator(Translator):
    dictionary = 	{"GetId":"+WWSNID"}

#Small testing
if __name__ == '__main__':
    t = RenesasTranslator()
    assert(t.tag("GetId") == "+WWSNID")
