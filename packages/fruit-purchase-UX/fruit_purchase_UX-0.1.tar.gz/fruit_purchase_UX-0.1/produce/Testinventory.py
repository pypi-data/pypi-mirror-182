import sys

sys.path.append("..")

import unittest
from produce.inventory import Inventory
from produce.fruit import Fruit

class TestInventory(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        pass
    
    def setUp(self):
        print('Set up of inventory module initiating')
        self.inv = Inventory()
        self.f1 = Fruit('Orange', 3, 30)

    def test_get_price(self):
        self.assertIsInstance(self.inv, Inventory)
        self.assertEqual(self.inv.get_price('Apple'), 10.5)
        self.assertNotIsInstance(self.inv, Fruit)
        self.assertEqual(self.f1.get_price(), 3)

    def test_get_discount(self):
        self.assertEqual(self.inv.get_discount('Apple'), 0.7)
        self.assertNotEqual(self.inv.get_discount('Apple'), 1)
        self.assertEqual(self.inv.get_discount('Orange'), 1)
        self.assertEqual(self.inv.get_discount('Pear'), 0.9)

    def tearDown(self):
        print('Testing of inventory module completed.')
    
    @classmethod
    def tearDownClass(self):
        pass
 
unittest.main(argv=[''], verbosity=2, exit=False)
