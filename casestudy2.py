#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # No of males and females participated in the test

# In[2]:


df = pd.read_csv('StudentsPerformance.csv')


# In[4]:


df['gender'].value_counts()


# # students' parental level of education

# In[5]:


df['parental level of education'].value_counts()


# # Who scores the most on average for math, reading and writing

# In[9]:


df['average'] = (df['math score'] + df['reading score'] + df['writing score'])/3


# In[10]:


df


# 1.gender

# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv('StudentsPerformance.csv')


# In[8]:


d1=df.groupby(['gender'])[['math score','reading score','writing score']].mean()
print(d2)


# 2.test preparation course

# In[9]:


d1=df.groupby(['test preparation course'])[['math score','reading score','writing score']].mean()
print(d1)


# # scoring variation for math, reading and writing

# 1.gender

# In[10]:


d3=df.groupby(['gender'])[['math score','reading score','writing score']].var()
print(d3)


# 2.test preparation course

# In[11]:


d4=df.groupby(['test preparation course'])[['math score','reading score','writing score']].var()
print(d4)


# # bonus points to the top 25%

# In[13]:


df3=df.sort_values(by=['math score'],ascending=False)
print(df3)


# In[14]:


n=0.25*1000
print('No.of students to be given bonus',n)
df4=df3.head(int(n))
print('Details of students to be given bonus=')
print(df4)


# In[ ]:




