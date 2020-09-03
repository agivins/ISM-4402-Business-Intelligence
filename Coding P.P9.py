#!/usr/bin/env python
# coding: utf-8

# In[23]:



import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])


# In[68]:


df.to_csv('studentgrades.csv',index=False,header=False) 


# In[69]:


df.head()


# In[70]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]

msdegrees = [2,1,0,0,0]

phddegrees = [0,1,0,0,0]

Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)

columns = ['Names','Grades','BS','MS','PhD']

df = pd.DataFrame(data = Degrees, columns=columns)


# In[71]:


df.thead()


# In[74]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/EDU02.xls"
df = pd.read_excel(Location)


# In[75]:


df.head()


# In[63]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[76]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/EDU02.xls"
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])


# In[77]:


df.to_csv('EDU02.xls',index=False,header=False) 


# In[78]:


df.head()


# In[ ]:




