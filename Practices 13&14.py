#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import numpy as np
import glob


# In[9]:


all_data = pd.DataFrame()
for f in glob.glob("C:/Users/Admin/Desktop/datasets/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[24]:


df.head()


# In[75]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:/Users/Admin/Desktop/datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))
sql = 'SELECT * from test where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[76]:


sql = "select name from sqlite_master"
"where type = 'table';"


# In[78]:


sql = "select * from test;"


# In[84]:


sales_data_df.head()


# In[ ]:





# In[87]:


import pandas as pd
import numpy as np
import glob


# In[ ]:


all_data = pd.DataFrame()
for f in glob.glob("C:/Users/Admin/Desktop/datasets/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()

