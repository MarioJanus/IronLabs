#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print(np.__version__)


# In[27]:


a = np.random.default_rng(1)
a = a.random((5, 2, 3))
print(a)


# In[20]:


a_alt1=np.random.random((5,2,3))
print(b)


# In[10]:


a_alt2=np.random.rand(5, 2, 3)
print(c)


# In[28]:


b=np.full((5, 2, 3), 1, dtype=int)


# In[23]:


print(b)


# In[ ]:


if a.any()==b.any():
    print("a and b are equal")
else:
    print('a and b are not equal')


# In[29]:


x = np.concatenate((a, b), axis=0)
print(x)


# In[ ]:




