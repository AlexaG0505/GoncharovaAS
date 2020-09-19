#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/u5WsfTX8rXb2phrNp (1 point)


# In[5]:


def calc_kinetic_energy(m, v):
	return round(0.5 * m * (v ** 2))


# In[6]:


Test.assert_equals(calc_kinetic_energy(60, 3), 270)
Test.assert_equals(calc_kinetic_energy(45, 10), 2250)
Test.assert_equals(calc_kinetic_energy(63.5, 7.35), 1715)


# In[ ]:




