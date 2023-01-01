#!/usr/bin/env python
# coding: utf-8

# Importing essential librariesm

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Reading CSV file

# In[2]:


df = pd.read_csv(r"C:\Users\UMAPRIYA\Desktop\Data Analyst_Naukri_Dataset\Final Dataset\Naukri_Data_Analyst_Jobs.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# There are 409 rows and 10 columns in the data set

# In[6]:


df.info()


# Overall information about the dataset

# In[7]:


df.describe()


# This shows the unique value,total count, top values and top value frequency per column

# In[8]:


df.isnull().sum()


# In[9]:


plt.figure(figsize=(10,2))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# Graph for showing the null values in a each column.
# 
# There is no missing values in this file

# In[10]:


import cufflinks as cf
cf.go_offline()


# In[11]:


df['Location'].value_counts()[0:7].iplot(kind='bar',colors='brown')


# To summarize above graph in short,the most jobs asre in Chennai

# In[12]:


df['Salary per annual'].value_counts()[0:8].iplot(kind='bar',colors='black')


# In[13]:


df['Experience'].value_counts()[0:17].iplot(kind='bar')


# To summarize above graph in short, There are around 41 jobs needs 3 to 8 year of job experience, 31 jobs which needs 5 to 10 years experience, 22 jobs with 3 to 6 years of experience.

# In[14]:


df['Job Type'].value_counts()[0:10].iplot(kind='bar',colors='red')


# To summarize above graph in short, There are around 361 jobs are Work from office, 32 jobs are Hybrid,13 jobs are Temp.WFH
# remaining jobs are Permanaent Remote.

# In[15]:


df['Job Role'].value_counts()[0:10].iplot(kind='bar',colors='green')


# This graph gives an top job role in naukri.com against the Data Analyst in Tamilnadu.

# In[16]:


df['Company'].value_counts()[0:20].iplot(kind='bar',colors='gold')


# This graph gives an Top hiring Company in Tamilnadu.

# In[17]:


df['Posted on'].value_counts()[0:20].iplot(kind='line',colors='blue')


# Above the graph shows the most of the jobs posted 30+ days ago.

# --------------------------------------------------------------------------------------------------------------------------
# 
# In short, according to given data, Data analyst jobs on Naukri.com are related to Data Science and Analytics industry against Tamilnadu filter and Most of the job recruiters are from Chennai region.
