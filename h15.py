#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Test:
	@staticmethod
	def assert_equals(a, b, *args, **kwargs):
		assert a == b
		print('Passed')


# In[ ]:


Problem https://edabit.com/challenge/XXJbGFEkrMWCp8yFn (1 point)


# In[2]:


def give_me_something(a):
	return "something" + " " + a


# In[3]:


Test.assert_equals(give_me_something("is better than nothing"), "something is better than nothing")
Test.assert_equals(give_me_something("Bob Jane"), "something Bob Jane")
Test.assert_equals(give_me_something("something"), "something something")


# In[ ]:




