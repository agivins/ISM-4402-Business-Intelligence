#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:/Users/Admin/Desktop/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:





# In[ ]:


#1.Max cars sold per month


# In[31]:


df["Cars Sold"].mean()


# In[ ]:





# In[ ]:


#2. Max cars sold per month


# In[30]:


df["Cars Sold"].max()


# In[ ]:





# In[ ]:


#3. Mins cars sold per month 


# In[29]:


df["Cars Sold"].min()


# In[ ]:





# In[ ]:


#4.Average cars sold per month by gender.


# In[27]:


df4=df[(df['Gender']=="F,M")]


# In[28]:


df["Cars Sold"].mean()


# In[ ]:





# In[ ]:


#5. Average hour worked by people selling more than three cars per month. 


# In[8]:


df1 =df[(df['Cars Sold'] >3)]


# In[9]:


df1["Hours Worked"].mean()


# In[ ]:





# In[ ]:


#6.Average years of experience


# In[17]:


df["Years Experience"].mean()


# In[ ]:





# In[ ]:


#7. Average years of experience for people selling more than three cars per month.


# In[22]:


df3 =df[(df['Cars Sold'] >3)]


# In[23]:


df3["Years Experience"].mean()


# In[ ]:





# In[ ]:


#8. Average cars sold per month sorted by whether they have had sales training. 


# In[12]:


df2 =df[(df['SalesTraining']=="Y" )]


# In[13]:


df2["Cars Sold"].mean()


# In[ ]:


#9. What do you think is the best indicator of whether someone is a good salesperson?


# In[ ]:


# The best indicator would be the number seven. Number seven display the average years of experience for people selling more than three cars per month.

