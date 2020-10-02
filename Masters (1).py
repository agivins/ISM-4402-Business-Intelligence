#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.head()


# In[3]:


# Create the bin dividers
bins = [0,80,100]
# Create names for the four groups
group_names = ['Fail','Pass']


# In[4]:


df[''] = pd.cut(df['grade'],bins, 
labels=group_names)
df


# In[5]:


df['Master'] = pd.cut(df['grade'],bins, 
labels=group_names)
df


# In[6]:


pd.value_counts(df[''])


# In[ ]:




