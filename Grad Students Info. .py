#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[38]:


df.head()


# In[42]:


# Create the bin dividers
bins = [0,80,100]
# Create names for the four groups
group_names = ['Fail','Pass']


# In[44]:


df[''] = pd.cut(df['grade'],bins, 
labels=group_names)
df


# In[45]:


pd.value_counts(df[''])


# In[49]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[50]:


bins = [0, 60, 70, 80, 90, 100]
group_names = ['F', 'D', 'C', 'B', 'A']
df['letterGrades'] = pd.cut(df['grade'],
bins, labels=group_names)
df.head()


# In[51]:


df.groupby('letterGrades')['hours'].mean()


# In[53]:


df['grade'] = df['grade'] = df['grade'].apply(lambda x: int(x))
df.head()


# In[55]:


gender_preScore = df['grade'].groupby(df['gender'])
gender_preScore.mean()


# In[87]:


# Create the bin dividers
bins = [0,70]
# Create names for the four groups
group_names = ['Fail','Pass']


# In[88]:


gender_preScore = df['grade'].groupby(df['gender'])
gender_preScore.mean()


# In[91]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[92]:


df['graderanked'] = df['grade'].rank(ascending=1)
df.tail()


# In[93]:


df[df['graderanked'] < 21]


# In[94]:


df[df['graderanked'] < 6].sort_values('graderanked')


# In[96]:


df[df['graderanked'] < 50].sort_values('hours')


# In[ ]:





# In[100]:


import pandas as pd
Location = "/Users/admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[101]:


import numpy as np
df['isFailing'] = np.where(df['grade']<70,
'yes', 'no')
df.tail(10)


# In[102]:


df['isFailingMale'] = np.where((df['grade']<70)
& (df['gender'] == 'male'),'yes', 'no')
df.tail(10)


# In[ ]:





# In[ ]:





# In[150]:


df['timemgmt'] = np.where((df['exercise']<3)
& (df['fname'] == 'hours'),'no','yes')
df.tail(10)


# In[153]:


df['timemgmt'] = np.where((df['hours']<3)
& (df['timemgmt'] == 'exercise'),'no','yes')
df.tail(10)


# In[154]:


df['timemgmt'] = np.where((df['hours']<17)
& (df['timemgmt'] == 'studies'),'no','yes')
df.tail(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[158]:


bins = [80, 90, 100]
group_names = ['B', 'A']
df['Master'] = pd.cut(df['grade'],
bins, labels=group_names)
df.head()


# In[160]:


df['Master'] = pd.cut(df['grade'],bins,
labels=group_names)
df


# In[161]:


pd.value_counts(df['Master'])


# In[ ]:




