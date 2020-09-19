#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/FQyaaJx7orS7tiwz8 (1 point)


# In[3]:


def convert(a):
	a *= 60
	return a


# In[4]:


Test.assert_equals(convert(5), 300)
Test.assert_equals(convert(3), 180)
Test.assert_equals(convert(2), 120)


# In[ ]:




