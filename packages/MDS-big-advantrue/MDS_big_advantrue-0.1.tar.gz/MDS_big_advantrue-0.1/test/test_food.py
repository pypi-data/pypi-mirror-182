import unittest
import sys
sys.path.insert(0, sys.path[0][:-4])
from MDS_Big_Adventure.item.food import item

class TestItem(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.i = item("bacon",20,30,2,2)
        
    def test_gethp(self):
        self.assertEqual(self.i.gethp(),20)
        self.assertNotEqual(self.i.gethp(),"bacon")
        self.assertNotEqual(self.i.gethp(),30)
        self.assertNotEqual(self.i.gethp(),2)
        
    def test_getprice(self):
        self.assertEqual(self.i.getprice(),2)
        self.assertNotEqual(self.i.getprice(),200)
        self.assertNotEqual(self.i.getprice(),-1)
        self.assertNotEqual(self.i.getprice(),100)
        
    def test_getpo(self):
        self.assertEqual(self.i.getpo(),30)
        self.assertNotEqual(self.i.getpo(),"bacon")
        self.assertNotEqual(self.i.getpo(),20)
        self.assertNotEqual(self.i.getpo(),2)
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

