#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/xWSjvoH7mEkSnqS7H (1 point)


# In[2]:


def calculate_exponent(a, b):
	return a ** b


# In[3]:


Test.assert_equals(calculate_exponent(5, 5), 3125)
Test.assert_equals(calculate_exponent(10, 10), 10000000000)
Test.assert_equals(calculate_exponent(3, 3), 27)


# In[ ]:




