#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


data = pd.read_csv(r"C:\Users\aniket.gope\Desktop\covid19_italy_region.csv")


# In[9]:


data.head()


# In[10]:


data.columns


# In[11]:


data.describe()


# In[15]:


data.isnull().sum()


# Relating the variables with scatterplots

# In[18]:


sns.relplot(x="TotalPositiveCases",y="Recovered",data = data)


# In[19]:


sns.relplot(x="TotalPositiveCases",y="Deaths",data = data)


# In[20]:


sns.pairplot(data)


# In[22]:


data.columns


# In[24]:


sns.relplot(x="HomeConfinement",y="TotalPositiveCases", kind = "line", data=data)


# In[ ]:


sns.catplot(x='Recovered', y ='TotalPositiveCases',data=data)


# In[ ]:




