#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


import pandas as pd


# In[7]:


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
df


# In[8]:


df.loc[df['Grades'] <= 100]


# In[16]:


df.loc[(df['Grades'] >= 100,'Grades')] =100
df.head()


# In[ ]:


import pandas as pd


# In[17]:


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,0,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
df


# In[18]:


df.loc[df['Grades'] <= 100]


# In[19]:


df.loc[(df['Grades'] >= 100,'Grades')] =100
df.head()


# In[ ]:




