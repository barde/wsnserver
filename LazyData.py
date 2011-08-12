#!/usr/bin/env python

#Lazy Data Singleton by Bartholomaeus Dedersen
#based on Alan Felice work
#Thread-safeness useless in project but kept
#for future expanse

import thread

class LazyData(object):
    '''Implement Pattern: SINGLETON'''

    __lockObj = thread.allocate_lock()  # lock object
    __instance = None  # the unique instance
    __content = ""

    def __new__(self):
        return self.getInstance()

    def __init__(self):
        pass

    def getInstance(self):
        '''Static method to have a reference to **THE UNIQUE** instance'''
        # Critical section start
        self.__lockObj.acquire()
        try:
            if self.__instance is None:
                # (Some exception may be thrown...)
                # Initialize **the unique** instance
                self.__instance = object.__new__(self)
		self.__content = ""
        finally:
            #  Exit from critical section whatever happens
            self.__lockObj.release()
        # Critical section end

        return self.__instance

    def getData(self):
        return self.__content
    def setData(self,data):
        self.__content = data

    content = property(getData, setData)
    getInstance = classmethod(getInstance)
