#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


female = df['gender'] == "female"
a_student = df['grade'] >= 90
df[female & a_student].head()


# In[4]:


df[df['fname'].notnull() & (df['gender'] == "male")]


# In[7]:


import pandas as pd
import numpy as np
Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.tail()


# In[8]:


df.take(np.random.permutation(len(df))[:100])


# In[9]:


df.take(np.random.permutation(len(df))[:500])


# In[10]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]


# In[11]:


GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
columns=['Names','Grades'])
df


# In[12]:


df['Grades'].count()# number of values
df['Grades'].mean()# arithmetic average
df['Grades'].std()# standard deviation
df['Grades'].min()# minimum
df['Grades'].max()# maximum
df['Grades'].quantile(.25)# first quartile
df['Grades'].quantile(.5) # second quartile
df['Grades'].quantile(.75)# third quartile


# In[13]:


# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
df['Grades'].mean()
# finds the median of the values in a column
# median = the middle value if they are sorted in order
df['Grades'].median()
# finds the mode of the values in a column
# mode = the most common single value
df['Grades'].mode()


# In[14]:


# computes the variance of the values in a column
df['Grades'].var()
df.var()


# In[15]:





# In[27]:


df['Grades'].mean()

df['Grades'].median()

df['Grades'].mode()
df['Grades'].var()
df.var()


# In[25]:


# the number of grades or the percentage of grades. 


# In[ ]:





# In[ ]:





# In[ ]:




