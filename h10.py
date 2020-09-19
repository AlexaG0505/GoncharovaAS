#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/gwqqc5p3oiFXRJAQm (1 point)


# In[2]:


def football_points(a, b, c):
	return 3*a + 1*b + 0*c


# In[3]:


Test.assert_equals(football_points(3, 4, 2), 13)
Test.assert_equals(football_points(5, 0, 2), 15)
Test.assert_equals(football_points(0, 0, 1), 0)


# In[ ]:




