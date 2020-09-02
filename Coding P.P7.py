#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/all_040_in_12.P1.csv"
df = pd.read_csv(Location, header=None)


# In[20]:


df.head()


# In[23]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/all_040_in_12.P1.csv"
df = pd.read_csv(Location)


# In[24]:


df.head()


# In[26]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/all_040_in_12.P1.csv"
df = pd.read_csv(Location, names=['Names','Grades'])


# In[27]:


df.head()


# In[ ]:




