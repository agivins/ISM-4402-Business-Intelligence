#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"


# In[3]:


df = pd.read_csv(Location)


# In[4]:


df.head()


# In[5]:


df.corr()


# In[15]:


import pandas as pd


# In[16]:


import numpy as np


# In[17]:


Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"


# In[18]:


df = pd.read_csv(Location)


# In[19]:


df.head()


# In[20]:


import statsmodels.formula.api as sm


# In[21]:


result = sm.ols(formula='grade ~ exercise + hours', data=df).fit()


# In[22]:


result.summary()


# In[ ]:




