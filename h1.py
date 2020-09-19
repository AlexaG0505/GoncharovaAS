#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/KjCS7occ9hfu5snpb (1 point)


# In[3]:


def addition(a):
	a += 1
	return a


# In[4]:


Test.assert_equals(addition(0), 1)
Test.assert_equals(addition(9), 10)
Test.assert_equals(addition(-3), -2)


# In[ ]:




