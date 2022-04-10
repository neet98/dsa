#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Find out how many countries are there in the dataset.

# In[3]:


df = pd.read_csv('Dataset_w6.xlsx - Data.csv')


# In[6]:


print("Number of countries in the dataset:",df.country.count())


# # Examine the data by using visualizations

# In[8]:


fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = df['GDP per capita (current US$)'], y = df['Agricultural production index '],c='orange', s=75,alpha=0.5)
plt.xlabel("GDP per capita (current US$)")
plt.ylabel("Agricultural production index ")
plt.title("GDP per capita with respect to Agricultural production index ")
plt.show()


# In[9]:


data1=df[['country','GDP per capita (current US$)']]
high_gdp=data1.nlargest(5,'GDP per capita (current US$)')
high_gdp.plot(kind='bar',x='country',figsize=(6,5),title='Top 5 GDP Countries',color='red')


# # Find out how many countries with respect to the region are available in the dataset

# In[10]:


df['Region'].value_counts()


# # On average which region has the highest

#  GDP per capita (current US$)

# In[12]:


high_dgp = df.groupby('Region')['GDP per capita (current US$)'].mean() 
high_dgp.nlargest(1)


#  International trade: Imports (million US$)

# In[13]:


high_imports = df.groupby('Region')['International trade: Imports (million US$)'].mean() 
high_imports.nlargest(1)


# # Find out which region has more consistent with respect to GDP per capita (current US$)

# In[14]:


std1 = df.groupby('Region')['GDP per capita (current US$)'].std() 
print("Region has more consistent with respect to GDP percapita (current US$) is:")
std1.nsmallest(1)


# In[ ]:




