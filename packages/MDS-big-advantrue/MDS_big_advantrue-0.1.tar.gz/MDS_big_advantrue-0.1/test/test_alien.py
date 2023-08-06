import unittest
import sys
sys.path.insert(0, sys.path[0][:-4])
from MDS_Big_Adventure.character.alien import alien

class TestAlien(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.a = alien(100,50,"monster",20)
        
    def test_getName(self):
        self.assertEqual(self.a.getName(),"monster")
        self.assertNotEqual(self.a.getName(),100)
        self.assertNotEqual(self.a.getName(),50)
        self.assertNotEqual(self.a.getName(),20)
        
    def test_dropMoney(self):
        self.assertEqual(self.a.dropMoney(),20)
        self.assertNotEqual(self.a.dropMoney(),200)
        self.assertNotEqual(self.a.dropMoney(),-1)
        self.assertNotEqual(self.a.dropMoney(),100)
    def test_die(self):
        self.a.die()
        self.assertEqual(self.a.health, 0)
    def test_isdead(self):
        self.a.die()
        self.assertTrue(self.a.isdead())
    def test_wound(self):
        self.a.wound(10)
        self.assertEqual(self.a.health, 90)
        self.a.wound(100)
        self.assertEqual(self.a.health, 0)
        
        
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

