#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/HQXRKxQXECFTCFTtn (1 point)


# In[2]:


def pos_com(a):
	return 2 ** a


# In[3]:


Test.assert_equals(pos_com(1), 2)
Test.assert_equals(pos_com(3), 8)
Test.assert_equals(pos_com(10), 1024)


# In[ ]:




