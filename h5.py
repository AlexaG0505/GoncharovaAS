#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


https://edabit.com/challenge/Zerwo2AENbvRZTe83 (1 point)


# In[2]:


def next_edge(a, b):
	return a + b - 1


# In[3]:


Test.assert_equals(next_edge(8, 10), 17)
Test.assert_equals(next_edge(5, 7), 11)
Test.assert_equals(next_edge(9, 2), 10)


# In[ ]:




