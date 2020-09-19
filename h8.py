#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT (1 point)


# In[2]:


def animals(a, b, c):
	return 2*a + 4*b + 4*c


# In[3]:


Test.assert_equals(animals(2, 3, 5), 36)
Test.assert_equals(animals(1, 2, 3), 22)
Test.assert_equals(animals(5, 2, 8), 50)


# In[ ]:




