#!/usr/bin/env python
# coding: utf-8

# In[32]:


import unittest

from main_package.Stock_main import *
from sub_package.bot import *


# In[33]:


class Testbot(unittest.TestCase): # test class
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    def setUp(self):
        print('Set up')

        
    def tearDown(self):
        print('Tear Down')

       
    def test_buy_stock_rp(self): # test case
        
        Stock1 = Stock()
        U2 = bot(Stock1)
        
        container_price_min = list(range(50,201))
        container_price_max = list(range(200,500))
        
        output = U2.buy_stock_rp(201, 50, vol=10)
         
        self.assertEqual(output[0],(10*output[1]))
        
        self.assertEqual(output[2],10)
        #try with 100, there will be assertion error
        
        self.assertIn(output[1],container_price_min)
        
        output = U2.buy_stock_rp(500, 200, vol=10)
        self.assertIn(output[1],container_price_max)
    
    def test_get_expense_list(self): # test case
        Stock1 = Stock()
        U2 = bot(Stock1)
        
        U2.process()
        
        out_expense = U2.get_expense_list()
        print(sum(out_expense))
        
        testval = (sum(out_expense) <= 10000.0)
        
        self.assertTrue(testval,"Expense > 10000")
        
         
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


# In[ ]:




