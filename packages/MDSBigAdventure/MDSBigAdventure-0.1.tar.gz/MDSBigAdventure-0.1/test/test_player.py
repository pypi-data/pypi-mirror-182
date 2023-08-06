import unittest
import sys
sys.path.insert(0, sys.path[0][:-4])
from MDS_Big_Adventure.character.player import player
from MDS_Big_Adventure.exceptions import InvalidPriceException
class TestPlayer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.p = player(100,50,1,1)
        
    def test_showMoney(self):
        self.assertEqual(self.p.showMoney(),1)
        self.assertNotEqual(self.p.showMoney(),100)
        self.assertNotEqual(self.p.showMoney(),50)
        self.assertNotEqual(self.p.showMoney(),-100)
        
    def test_getidentity(self):
        self.assertEqual(self.p.getidentity(),1)
        self.assertNotEqual(self.p.getidentity(),0)
        self.assertNotEqual(self.p.getidentity(),2)
        self.assertNotEqual(self.p.getidentity(),3)
        
    def test_pay(self):
        self.assertEqual(self.p.pay(-0.1), "Price can't be negative")
        self.assertEqual(self.p.pay("1"), "Price has to be a number")
        self.p.pay(1)
        self.assertEqual(self.p.money, 0)
        
    
    
    def test_getMoney(self):
        self.p.getMoney(5)
        self.assertEqual(self.p.showMoney(), 6)
        self.p.getMoney("abc")
        self.assertEqual(self.p.showMoney(), 6)
        
    def test_advance(self):
        self.p.advance()
        self.assertEqual(self.p.position, 1)
        self.p.advance()
        self.p.advance()
        self.p.advance()
        self.p.advance()
        self.assertEqual(self.p.position, 4)
        
    def test_retreat(self):
        self.p.retreat()
        self.assertEqual(self.p.position, 0)
        self.p.advance()
        self.p.retreat()
        self.assertEqual(self.p.position, 0)
        
    def test_wound(self):
        self.p.wound(10)
        self.assertEqual(self.p.health, 90)
        self.p.wound(100)
        self.assertEqual(self.p.health, 0)
        
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

