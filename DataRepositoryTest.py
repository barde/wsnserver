'''
DataRepositoryTest
This class is used to test the repository
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
    
    def testRemoveAllData(self):
        dr = DataRepository.DataRepository()
        dr.removeAllData()
        self.assertEqual(0, len(dr.readAllData("wsn01")), 
                         "RemoveAllData failed")
       
    def testRemoveFromDB(self):
        dr = DataRepository.DataRepository()
        self.assertTrue(dr.removeFromDB(), "RemoveFromDB failed")

    def testReadAllData(self):
        dr = DataRepository.DataRepository()
        self.assertEqual(1, len(dr.readAllData("wsn01")), 
                         "ReadAllFromDB failed")
      
    def testReadLeatestFromDB(self):
        dr = DataRepository.DataRepository()
        self.assertTrue(dr.readLeatestFromDB(), "ReadLeatestFromDB failed")
        
    def testSaveData(self):
        dr = DataRepository.DataRepository()
        dr.saveData("wsn01", "testdata")
        self.assertEqual(2, len(dr.readAllData("wsn01")), "SaveToDB failed")

    def tearDown(self):
        DataRepository.DataRepository().removeAllData()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()