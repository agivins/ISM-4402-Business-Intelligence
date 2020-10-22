#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[40]:


Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"


# In[41]:


df = pd.read_csv(Location)
df.head()
df.mode().transpose()


# In[ ]:





# In[ ]:





# In[ ]:


data_types = pd.DataFrame(df.dtypes,
                          columns=['Data Type'])


# In[27]:


data_types


# In[28]:


missing_data_counts = pd.DataFrame(df.isnull().sum(),
                                   columns=['Missing Values'])
missing_data_counts


# In[29]:


present_data_counts = pd.DataFrame(df.count(),
                                   columns=['Present Values'])
present_data_counts


# In[30]:


unique_value_counts = pd.DataFrame(
    columns=['Unique Values'])
for v in list(df.columns.values):
    unique_value_counts.loc[v] = [df[v].nunique()]
unique_value_counts


# In[31]:


minimum_values = pd.DataFrame(columns=[
    'Minimum Values'])
for v in list(df.columns.values):
    minimum_values.loc[v] = [df[v].min()]
minimum_values


# In[32]:


maximum_values = pd.DataFrame(
    columns=['Maximum Values'])
for v in list(df.columns.values):
    maximum_values.loc[v] = [df[v].max()]
maximum_values


# In[33]:


pd.concat([present_data_counts,
           missing_data_counts,
           unique_value_counts,
           minimum_values,
           maximum_values],
          axis=1)


# In[51]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


5-11


# In[ ]:





# In[77]:


df.plot()
displayText = "my annotation"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150
plt.annotate(displayText,
             xy=(xloc, yloc),
             arrowprops=dict(facecolor='black',
                             shrink=0.05),
             xytext=(xtext,ytext),
xycoords=('axes fraction', 'data'),
textcoords='offset points')


# In[ ]:





# In[ ]:


Take the same dataset we used in this example and add an annotation to Bob's 76 that says “Wow!”


# In[78]:


df.plot()
displayText = "WoW"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150
plt.annotate(displayText,
             xy=(xloc, yloc),
             arrowprops=dict(facecolor='black',
                             shrink=0.05),
             xytext=(xtext,ytext),
xycoords=('axes fraction', 'data'),
textcoords='offset points')


# In[ ]:





# In[ ]:





# In[66]:


import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[ ]:





# In[67]:


df2 = df.set_index(df['Names'])
df2.plot(kind="bar")


# In[ ]:


get_ipython().set_next_input('Can you change the code to create a bar plot where the status is the label');get_ipython().run_line_magic('pinfo', 'label')


# In[ ]:





# In[68]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
gender = ['Male','Female','Female','Male','Female']
status = ['Senior','Senior','Junior','Junior','Senior']
GradeList = zip(names,grades,gender)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades', 
                                             'Gender'])
df.boxplot(column='Grades')


# In[69]:


df.boxplot(by='Gender', column='Grades')


# In[ ]:




