import unittest
import sys
sys.path.insert(0, sys.path[0][:-4])
from MDS_Big_Adventure.scene.level import level

class TestLevel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.l = level(0,["plot A","plot B"],"monster")
        
    def test_getStatus(self):
        self.assertEqual(self.l.getStatus(),0)
        self.assertNotEqual(self.l.getStatus(),1)
        self.assertNotEqual(self.l.getStatus(),50)
        self.assertNotEqual(self.l.getStatus(),20)
        
    def test_getLoc(self):
        self.assertEqual(self.l.getLoc(),0)
        self.assertNotEqual(self.l.getLoc(),200)
        self.assertNotEqual(self.l.getLoc(),-1)
        self.assertNotEqual(self.l.getLoc(),100)
        
    def test_getplot(self):
        self.assertEqual(self.l.getplot(),"plot A")
        self.l.visit()
        self.assertEqual(self.l.getplot(),"plot B")
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

