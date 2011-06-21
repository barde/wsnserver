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
        dr.saveToDB("data", "testdata", "tester")
    
    def testRemoveAllFromDB(self):
        dr = DataRepository.DataRepository()
        dr.removeAllFromDB()
        self.assertEqual(0, len(dr.readAllFromDB("tester")), 
                         "RemoveAllFromDB failed")
       
    def testRemoveFromDB(self):
        dr = DataRepository.DataRepository()
        self.assertTrue(dr.removeFromDB(), "RemoveFromDB failed")

    def testReadAllFromDB(self):
        dr = DataRepository.DataRepository()
        self.assertEqual(1, len(dr.readAllFromDB("tester")), 
                         "ReadAllFromDB failed")
      
    def testReadLeatestFromDB(self):
        dr = DataRepository.DataRepository()
        self.assertTrue(dr.readLeatestFromDB(), "ReadLeatestFromDB failed")
        
    def testSaveToDB(self):
        dr = DataRepository.DataRepository()
        dr.saveToDB("data", "test", "tester")
        self.assertEqual(2, len(dr.readAllFromDB("tester")), "SaveToDB failed")

    def tearDown(self):
        DataRepository.DataRepository().removeAllFromDB()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()