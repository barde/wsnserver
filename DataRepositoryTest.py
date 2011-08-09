'''
Name: DataRepositoryTest
Purpose: This class is used to test the repository
Created on 20.06.2011
@author: Kamil Wozniak
'''
import unittest
import DataRepository


class DataRepositoryTest(unittest.TestCase):
    
    ''' Setup sets up the fixtures in the database for every testrun '''
    def setUp(self):
        dr = DataRepository.DataRepository()
        dr.saveData("wsn01", "testdata")
        dr.saveCMD("wsn01", "pause")
        
    def testReadCMD(self):
        dr = DataRepository.DataRepository()
        dr.saveCMD("wsn01", "pause")
        self.assertEqual(1, len(dr.readCMD("wsn01")), 
                         "ReadCMD does not work.")
    
    def testSaveCMD(self):
        dr = DataRepository.DataRepository()
        dr.saveCMD("wsn01", "pause")
        self.assertEqual(1, len(dr.readCMD("wsn01")), 
                         "SaveCMD does not work.")
        
    def testRemoveAllCMD(self):
        dr = DataRepository.DataRepository()
        dr.removeAllCMD()
        self.assertEqual(0, len(dr.readCMD("wsn01")), 
                         "removeAllCMD does not work.")
    
    def testRemoveAllData(self):
        dr = DataRepository.DataRepository()
        dr.removeAllData()
        self.assertEqual(0, len(dr.readAllData("wsn01")),
                         "RemoveAllData failed")

    def testReadAllData(self):
        dr = DataRepository.DataRepository()
        self.assertEqual(1, len(dr.readAllData("wsn01")),
                         "ReadAllFromDB failed")
      
    def testReadLeatestData(self):
        dr = DataRepository.DataRepository()
        self.assertEqual(1, len(dr.readLeatestData("wsn01")), 
                         "ReadLeatestFromDB failed")
        
    def testSaveData(self):
        dr = DataRepository.DataRepository()
        dr.saveData("wsn01", "testdata")
        self.assertEqual(2, len(dr.readAllData("wsn01")), "SaveToDB failed")

    def tearDown(self):
        dr = DataRepository.DataRepository()
        dr.removeAllData()
        dr.removeAllCMD()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
