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

class Translator:
	__renesas = 	{"key":"value",
			"key2":"value"}

	def __init__(self, wsnType):
		self.wsnType = wsnType
