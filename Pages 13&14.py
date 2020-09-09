#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob


# In[4]:


all_data = pd.DataFrame()
for f in glob.glob("C:/Users/Admin/Desktop/datasets/salesdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[5]:


df.head()


# In[10]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:/Users/Admin/Desktop/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))
sql = 'SELECT * from test where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[11]:


sql = "select name from sqlite_master"
"where type = 'table';"


# In[12]:


sql = "select * from test;"


# In[13]:


sales_data_df.head()


# In[ ]:




