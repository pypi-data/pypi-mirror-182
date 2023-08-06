import sys

sys.path.append("..")

import unittest
from produce.fruit import Apple, Banana

class TestFruit(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        pass
    
    def setUp(self):
        print('Set up of fruit module initiating')
        self.apple = Apple(10,24)
        self.banana = Banana(8,30) 

    def test_get_price_discount(self):        
        self.assertEqual(self.apple.get_name(), 'Apple')
        self.assertEqual(self.apple.get_price(), 10)
        self.assertEqual(self.apple.get_discount(), 1)
        self.assertEqual(self.banana.get_discount(), 1)        
        
    def test_get_expiry_inventory(self):
        self.assertEqual(self.apple.get_expiry(), 7)
        self.assertEqual(self.apple.get_inventory(), 24)
        self.assertEqual(self.apple.get_inventory(), 24)
        self.assertEqual(self.apple.sale(20), 200)
        

    def tearDown(self):
        print('Testing of fruit module completed.')
        
    @classmethod
    def tearDownClass(self):
        pass
 
unittest.main(argv=[''], verbosity=2, exit=False)
