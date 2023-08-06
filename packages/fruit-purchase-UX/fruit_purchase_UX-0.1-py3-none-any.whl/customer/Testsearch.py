import sys

sys.path.append("..")

import unittest
from customer.Search import Search 
from customer.Customer import Customer

class TestSearch(unittest.TestCase):
    
    @classmethod
    def setUpclass(self):
        pass
    
    def setUp(self):
        print('Set up of search module initiating')
        self.cust1 = Customer()
        self.cust1.shop_item('Apple',10)
        self.cust1.shop_item('Pear',5)
        self.s1 = Search()
        self.s1.set_customer(self.cust1)

    def test_fruit_detail(self):       
        self.assertIsInstance(self.s1, Search)
        self.assertEqual(self.s1.sales(), 250)
        self.assertEqual(self.s1.get_price('Pear'), 18)
        self.assertEqual(self.s1.get_discount('Apple'), 0.7)
        self.assertEqual(self.s1.get_current_price(), (False, 250))
        self.assertEqual(self.s1.fruit_detail('Apple'), True)
        
    def test_customer_detail(self):
        self.assertIsInstance(self.cust1, Customer)
        self.assertEqual(self.cust1.items_detail(), None)
        self.assertEqual(self.cust1.get_items(), {'Pear': 5, 'Apple': 10})
        self.assertEqual(self.cust1.items_detail(), None)        

    def tearDown(self):
        print('Testing of search module completed.')
        
    @classmethod
    def tearDownclass(self):
        pass
 
unittest.main(argv=[''], verbosity=2, exit=False)
