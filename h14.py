#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/dcdy9QMBbryyWENcm (1 point)


# In[2]:


def total_cups(n):
	return n//6 + n


# In[3]:


Test.assert_equals(total_cups(6), 7)
Test.assert_equals(total_cups(12), 14)
Test.assert_equals(total_cups(213), 248)


# In[ ]:




