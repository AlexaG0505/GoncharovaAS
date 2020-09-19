#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/aWLTzrRsrw7RakYrN (1 point)


# In[2]:


def tri_area(a, h):
	return a*h/2


# In[3]:


Test.assert_equals(tri_area(3, 2), 3)
Test.assert_equals(tri_area(7, 4), 14)
Test.assert_equals(tri_area(10, 10), 50)


# In[ ]:




