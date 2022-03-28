#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('cars_data.csv')
data.head()


# # Check for the null values present in the dataset

# In[3]:


data_null=data.isnull().sum()
print("The null values present in the dataset:")
data_null


# # Bar graph of male vs female buyers participated in the sales.

# In[8]:


data['Buyer Gender'].value_counts().plot(kind='bar',width = 0.1,figsize=(5,5),color=['orange', 'yellow'],edgecolor='red');
plt.ylim(4500,5200)
plt.xlabel("Gender", labelpad=14)
plt.ylabel("Count of People", labelpad=14)
plt.title("Count of male vs female buyers participated in the sales",fontsize=16, y=1.02);


# # Top 5 cars based on their sales price.

# In[5]:


data1 = data.sort_values(by=["Sale Price"],ascending=False)
print("Top 5 cars based on sale price are:")
data1.filter(['Model','Sale Price']).head().style.hide_index()


# # Least 5 cars based on their Resell price.

# In[6]:


data1 = data.sort_values(by=["Resell Price"])
print("Least 5 cars based on Resell Price are:")
data1.filter(['Model','Resell Price']).head().style.hide_index()


# In[ ]:




