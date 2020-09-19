#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/nyeNvKWdDFKRAk4Da (1 point)


# In[8]:


def how_many_seconds(a):
	a *= 3600
	return a


# In[9]:


Test.assert_equals(how_many_seconds(2), 7200)
Test.assert_equals(how_many_seconds(10), 36000)
Test.assert_equals(how_many_seconds(24), 86400)


# In[ ]:




