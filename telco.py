#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None


# In[2]:


data = pd.read_csv("Telco-Customer-Churn.xlsx - Telco-Customer-Churn.csv")


# In[4]:


data = pd.read_csv("Telco-Customer-Churn.xlsx - Telco-Customer-Churn.csv")
data.head()


# # Compare churn count with respect to gender.

# In[17]:


sns.countplot(data=data,x='gender',hue='Churn',palette=['orange',"green"])
plt.title("Churn count with respect to gender")


# # Find out how many female senior citizens there in the dataset

# In[20]:


df=data[data.gender == 'Female']
df.loc[df.SeniorCitizen==1,'SeniorCitizen'] = "Yes"
df.loc[df.SeniorCitizen==0,'SeniorCitizen'] = "No"
sns.countplot(x ='gender', hue = "SeniorCitizen", data = df,palette='dark')
sns.despine()
plt.title( "Female senior citizens there in the dataset") 
plt.xlabel('')
plt.ylabel('Count') 


# # Compare tenure with Total Charges

# In[9]:


sns.lineplot(data=data, x="tenure", y="TotalCharges",color='green', linewidth=2.5)


# # Find out which contract is preferred by the senior citizen.

# In[14]:


sn= data[data["SeniorCitizen"]==1]
plt.figure(figsize=(6,6))
plt.title( "Distribution of contract is preferred by the senior citizens",fontsize=16) 
sn.Contract.value_counts(sort=True).plot.pie(autopct ='%1.1f',colors = ['red','green','violet'])
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.show()


# # Payment Method based on gender

# In[22]:


plt.figure(figsize=(10,7))
sns.countplot(data[ 'PaymentMethod' ], hue=data[ 'gender'],palette='Set1')
sns.despine()
plt.title( "Payment Method based on gender",fontsize=16) 
plt.xlabel('Payment Method')
plt.ylabel('Count') 


# In[ ]:




