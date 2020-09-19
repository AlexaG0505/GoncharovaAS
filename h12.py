#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/MaekZ28kEvH9ZxPga (1 point)


# In[2]:


def cube_squareroot(a):
	return (a ** 3) ** 0.5


# In[3]:


Test.assert_equals(cube_squareroot(81), 729)
Test.assert_equals(cube_squareroot(1646089), 2111932187)
Test.assert_equals(cube_squareroot(695556), 580093704)


# In[ ]:




