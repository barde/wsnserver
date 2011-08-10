#!/usr/bin/env python

#Lazy Data Singleton by Bartholomaeus Dedersen

class LazyData:
        __lazyData = ""
        def _call(self):
                return self
        def getData(self):
                return self.__lazyData
        def setData(self,data):
                __lazyData = data
        content = property(getData, setData)
