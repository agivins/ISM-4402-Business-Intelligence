#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


import numpy as np


# In[13]:


Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"


# In[14]:


df = pd.read_csv(Location)


# In[15]:


df.head()


# In[26]:


df['Gender'] = np.where(df['gender']!= 'male', 1 ,0)


# In[ ]:





# In[27]:


df.head()


# In[23]:


import statsmodels.formula.api as sm


# In[19]:


result = sm.ols(formula='grade ~ exercise + hours', data=df).fit()


# In[20]:


result.summary()


# In[ ]:




