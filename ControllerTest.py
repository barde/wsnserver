'''
Name: ControllerTest
Purpose: This class is used to test the controller
Created on 02.08.2011
@author: Kamil Wozniak
'''
import unittest
import Controller
import DataRepository

class ControllerTest(unittest.TestCase):
    
    ''' 
    Create new instance of the controller and the datarepository for the tests. 
    Only one instance of each class is needed, so they are outside the setUp method.
    '''
    controller = Controller.Controller()
    dataRepository = DataRepository.DataRepository()
    
    def setUp(self):
        ''' 
        DataRepository is directly used for fixtures. 
        '''
        self.dataRepository.saveData("wsn01", "10")

    def testReadCMDAction(self):
        pass
    
    def testSaveCMDAction(self):
        pass
    
    def testSaveDeviceAction(self):
        self.controller.saveDeviceAction("wsn01", "0xACE", "5")
        self.assertEqual(1, len(self.dataRepository.readDeviceList()), "Saving the devices failed.")
        
    def testSaveDeviceActionWithEmptyParams(self):
        self.controller.saveDeviceAction("", "", "")
        self.assertEqual(0, len(self.dataRepository.readDeviceList()), "Parameters have not been recognized.")
        
    def testReadDeviceList(self):
        self.controller.saveDeviceAction("wsn01", "0xACE", "5")
        devices = self.controller.readDeviceList()
        self.assertEqual("wsn01", devices[0][0], "Devices on the list failed.")
    
    def testSaveDataAction(self):
        self.controller.saveDataAction("wsn01", "15")
        ''' Must be equal 2 because one dataset is being added by the setUp method. '''
        self.assertEqual(2, len(self.dataRepository.readAllData("wsn01")), "SaveDataAction failed.")
    
    def testReadAllAction(self):
        pass
    
    def testReadLeatestAction(self):
        self.controller.readLeatestAction("wsn01")
    
    def testRemoveAllDataAction(self):
        self.controller.removeAllDataAction()
        self.assertEqual(0, len(self.dataRepository.readAllData("wsn01")), 
                         "RemoveAllAction does not work properly.")
        
    def tearDown(self):
        ''' Remove all data/devices/cmds from db before next test. '''
        self.dataRepository.removeAllData()
        self.dataRepository.removeAllDevices()
        self.dataRepository.removeAllCMD()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
