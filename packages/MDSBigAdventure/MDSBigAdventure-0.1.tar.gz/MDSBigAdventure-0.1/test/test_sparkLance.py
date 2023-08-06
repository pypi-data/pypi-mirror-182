import unittest
import sys
sys.path.insert(0, sys.path[0][:-4])
from MDS_Big_Adventure.item.sparkLance import sparkLance

class TestSparkLance(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("")
    
    def setUp(self):
        self.s = sparkLance("sparkLance",20,30,0)
        
    def test_getstatus(self):
        self.assertEqual(self.s.getstatus(),0)
        self.assertNotEqual(self.s.getstatus(),1)
        self.assertNotEqual(self.s.getstatus(),30)
        self.assertNotEqual(self.s.getstatus(),2)
        
    def test_getplot(self):
        self.assertEqual(self.s.getplot(),["""
                                          As soon as you touched the Spark Lance, it started glowing and immersed you in light.
                                          You were startled at first, but soon you felt something, something strange but familiar.
                                          It felt like those sunny afternoons, when you look out from the window, 
                                          everything is so quite under the clear blue sky, you feel peaceful. 
                                          It then felt like the times when you finished the very last exam of the term, you are relieved, and hope
                                          is coming back to you agian.
                                          After that, you felt courage, it was like recieving an quiz score better than you had hoped, you started to believe
                                          in yourself.

                                          Suddenly, You heard a voice in the light: 

                                          "The only way to save the world, is you become the light"

                                          Yes, I can be the light! You thought.

                                          You raised the Spark Lance high:

                                          Ultraman !!!!!!!!!!

                                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Exciting BGM playing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                          *********************************************Fancy visual effects *************************************************

                                          You transformed into Ultraman with the power of the light, you now have special powers to save the world.
                          """,
                """
                                           "It is you..." The Tim Hortons staff said slowly.
                                           "Many years ago an old lady came here and ordered turkey bacon club,
                                           I told her we only have breakfast at this branch, but she came back again
                                           the following day and ordered the same thing. After I told her the
                                           that we really don't sell turkey bacon here, she smiled and gave something to me, wait here please." 
                                           The staff hurried into the storage room. He came back with a strange looking artifact in his hand.
                                           
                                           Strangly, your attantion is captured by it, as if it is speaking to you.
                                           
                                           "This is Spark Lance," said the staff, "the old lady said if one day this world is
                                           in trouble, someone would come here to order turkey bacon club, I should tell that
                                           person the same thing I told her at the first time. If that person came back again, 
                                           I should give this to them." 
                                           
                                           The Tim Horton's staff handed the artifact to you"""])
        self.assertNotEqual(self.s.getplot(),200)
        self.assertNotEqual(self.s.getplot(),-1)
        self.assertNotEqual(self.s.getplot(),100)
        
    def test_check(self):
        self.s.check()
        self.assertEqual(self.s.getstatus(), 1)
    
    def test_betaTransform(self):
        class p():
            def __init__(self, health):
                self.health = health
        self.p = p(10)
        
        self.s.betaTransform(self.p)
        
        self.assertEqual(self.p.health, 10*20)
        self.s.betaTransform(10)
        
    def tearDown(self):
        print("")
        
    @classmethod
    def tearDownClass(cls):
         print("")
         
    unittest.main(argv=[''], verbosity=2, exit=False)   

