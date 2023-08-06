#!/usr/bin/env python
# coding: utf-8

# In[26]:


import unittest

from sub_package.endgame import *


# In[31]:


class Testendgame(unittest.TestCase): # test class
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    def setUp(self):
        print('Set up')

        
    def tearDown(self):
        print('Tear Down')

       
    def test_cashback(self): # test case
        player_1_status = [[100,0,0,100], [10,10,10,10], [10,0,0,10]]
        dobby_2_status = [[0,100,0,100], [10,10,10,10], [0,10,0,10]]      

        (cb_t1, cb_t2) = cashback(player_1_status, dobby_2_status)
 
        self.assertEqual(cb_t1, [0, 100, 0, 0])
        
        self.assertEqual(cb_t2,[100, 0, 0, 0])
        
        
       
        #check for minimum rounds which is 1
        
        player_1_status = [[100], [10], [10]]
        dobby_2_status = [[0], [10], [0]]
        
        (cb_t3, cb_t4) = cashback(player_1_status, dobby_2_status)

        self.assertEqual(cb_t3, [0])
        
        self.assertEqual(cb_t4, [100])
        
    def test_final_price(self): # test case
        # check there is 4 values in the output list and all between high and low range
        player_1_status = [[100,0,0,100], [10,10,10,10], [10,0,0,10], [0, 100, 0, 0]]
        dobby_2_status = [[0,100,0,100], [10,10,10,10], [0,10,0,10], [100, 0, 0, 0]]
        stock_list = [[120,120,120,120], [50,50,50,50], 4]
       

        sell_price_t1 = final_price(player_1_status, stock_list)
        #print(sell_price_t1)
        container_price_min = list(range(50,120))
        
        self.assertIn(sell_price_t1[0],container_price_min)
        self.assertIn(sell_price_t1[1],container_price_min)
        self.assertIn(sell_price_t1[2],container_price_min)
        self.assertIn(sell_price_t1[3],container_price_min)
        self.assertEqual(len(sell_price_t1), 4)
        
             
            
        #check for minimum rounds which is 1
        
        player_1_status = [[100], [10], [10]]
        dobby_2_status = [[0], [10], [0]]
        stock_list = [[120], [50], 1]
        
        sell_price_t2 = final_price(player_1_status, stock_list)
        #print(sell_price_t1)
        self.assertIn(sell_price_t2[0],container_price_min)
         
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


# In[ ]:




