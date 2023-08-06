#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
from Test_bot import *
from Test_endgame import *
from Test_Stock_Main import *
from Test_User import *

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    #add for each of the py files created with test case
    suite.addTest(unittest.makeSuite(TestStock))
    suite.addTest(unittest.makeSuite(TestUser))
    suite.addTest(unittest.makeSuite(Testbot))
    suite.addTest(unittest.makeSuite(Testendgame))
    #runner = unittest.TextTestRunner()
    return suite
    
#print(runner.run(suite))

#my_suite()


# In[3]:


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(my_suite())


# In[ ]:




