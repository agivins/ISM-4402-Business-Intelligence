#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.hist(column="hours", by="gender")


# In[ ]:





# In[ ]:





# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[11]:


df['TotalDemerits'] = df['Absences'] +df['Detentions'] + df['Warnings']
df


# In[12]:


plt.pie(df['TotalDemerits'])


# In[13]:


plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0,0.15),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[14]:


plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0,0.15),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[ ]:





# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
                          np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[ ]:





# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/Admin/Desktop/datasets/gradedata.csv"
dataframe = pd.DataFrame({'Col':
                          np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[ ]:




