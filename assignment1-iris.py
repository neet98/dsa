#!/usr/bin/env python
# coding: utf-8

# # Read Dataset

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data_iris = pd.read_csv("iris.csv")


# In[5]:


data_iris = pd.read_csv("iris.csv")
data_iris.head()


# # display columns

# In[6]:


data_iris.columns 


# # To find Mean

# In[8]:


data_iris.iloc[:,0:4].apply(np.mean)


# # to find null values

# In[14]:


import pandas as pd
import numpy as np
data_iris= pd.read_csv("iris.csv")


# In[15]:


data_iris


# In[16]:


data_iris.isnull().sum()


# In[17]:


data_iris['Classification'].value_counts()


# # Data Analysis

# # Scatterplot

# In[18]:


colors=['red','green','blue']
Classification=['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in range(3):
  x=data_iris[data_iris['Classification']==Classification[i]]
  plt.scatter(x['SL'],x['SW'],c = colors[i], label=Classification[i])
plt.xlabel('SEPAL LENGTH')
plt.ylabel('SEPAL WIDTH')
plt.legend()


# In[19]:


colors=['red','green','blue']
Classification=['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in range(3):
  x=data_iris[data_iris['Classification']==Classification[i]]
  plt.scatter(x['PL'],x['PW'],c = colors[i], label=Classification[i])
plt.xlabel('PETAL LENGTH')
plt.ylabel('PETAL WIDTH')
plt.legend()


# In[20]:


colors=['red','green','blue']
Classification=['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in range(3):
  x=data_iris[data_iris['Classification']==Classification[i]]
  plt.scatter(x['PL'],x['SW'],c = colors[i], label=Classification[i])
plt.xlabel('PETAL LENGTH')
plt.ylabel('SEPAL WIDTH')
plt.legend()


# In[21]:


colors=['red','green','blue']
Classification=['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in range(3):
  x=data_iris[data_iris['Classification']==Classification[i]]
  plt.scatter(x['SL'],x['PW'],c = colors[i], label=Classification[i])
plt.xlabel('SEPAL LENGTH')
plt.ylabel('PETAL WIDTH')
plt.legend()


# # Insights

# In[ ]:


1) The classification Iris-setosa has lower sapal length,low petal width and petal length and a high sepalwidth.

2) The classification Iris -virginica has high petal length and petal width. 

3) The classification Iris -versicolor has medium range of petal width and petal length

