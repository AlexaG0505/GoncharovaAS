#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/KWoj7kWiHRqJtG6S2 (1 point)


# In[2]:


def remainder(a, b):
	return a % b


# In[3]:


Test.assert_equals(remainder(1, 3), 1)
Test.assert_equals(remainder(3, 4), 3)
Test.assert_equals(remainder(5, 5), 0)
Test.assert_equals(remainder(7, 2), 1)


# In[ ]:




