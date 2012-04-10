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

#Abstract class
class Translator:
    dictionary =	{"UniversalLangugeTag":"SpecificDeviceTag"}

    def tag(self,genericCommand):
        for tag in self.dictionary:
            if tag == genericCommand:
                return self.dictionary[tag]
        return "No dictionary entry found!"
        
#First real dictionary as inherited class
class RenesasTranslator(Translator):
    dictionary =	{
					"GetId":"+WWSNID\n\r", 
					"GetChannel":"+WCHAN\n\r",
					"GetPanId":"+WPANID\n\r",
					"LedOn":"+WLED1 ON\n\r",
					"LedOff":"+WLED1 OFF\n\r",
					"TempOn":"+WSENDTEMP\n\r",
					"TempOff":"+WNSENDTEMP\n\r",
					"Enquiry":"+WENQ\n\r"
					}

class MedusaTranslator(Translator):
	dictionary =	{
					"GetId":"COUNTHEADS",
					"CountChildren":"LOCALIZE"
					}


#Small testing
if __name__ == '__main__':
    t = RenesasTranslator()
    assert(t.tag("GetId") == "+WWSNID\n\r")
