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
    
    ''' Create new instance of controller for the tests. '''
    controller = Controller.Controller()
    dataRepository = DataRepository.DataRepository()
    
    def setUp(self):
        ''' DataRepository is directly used for fixtures. '''
        self.dataRepository.saveData("wsn01", "10")

    def testReadCMDAction(self):
        pass
    
    def testSaveCMDAction(self):
        pass
    
    def testSaveDataAction(self):
        self.controller.saveDataAction("wsn01", "15")
        ''' Must be equal 2 because one dataset is being added by the setUp method. '''
        self.assertEqual(2, len(self.dataRepository.readAllData("wsn01")), "SaveDataAction failed.")
    
    def testReadAllAction(self):
        pass
    
    def testReadLeatestAction(self):
        pass
    
    def testRemoveAllAction(self):
        self.controller.removeAllAction()
        self.assertEqual(0, len(self.dataRepository.readAllData("wsn01")), 
                         "RemoveAllAction does not work properly.")
        
    def tearDown(self):
        ''' Remove all data from db before next test. '''
        self.dataRepository.removeAllData()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()