#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/Yx2a9B57vXRuPevGh (1 point)


# In[2]:


def find_perimeter(a, b):
	return 2 * (a + b)


# In[3]:


Test.assert_equals(find_perimeter(6, 7), 26)
Test.assert_equals(find_perimeter(20, 10), 60)
Test.assert_equals(find_perimeter(2, 9), 22)


# In[ ]:




