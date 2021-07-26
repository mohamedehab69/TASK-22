#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('911.csv')
df


# In[4]:


df.head()


# In[5]:


df = df.drop('e',axis=1)


# In[6]:


df.info()


# In[8]:


df['reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[9]:


df['title_code'] = df['title'].apply(lambda title: title.split(':')[1])


# In[10]:


fig, axes = plt.subplots(1,2, figsize=(15, 5))

sns.countplot(x='reason', data=df, order=df['reason'].value_counts().index, ax=axes[0])
axes[0].set_title('Common Reasons for 911 Calls', size=13)
axes[0].set(xlabel='Reason', ylabel='Count')

df['reason'].value_counts().plot.pie(autopct='%1.1f%%',ax=axes[1],shadow=True)
axes[1].set(xlabel='', ylabel='')

sns.despine(bottom=False, left=True)


# In[11]:


fig, axes = plt.subplots(figsize=(10, 5))
sns.countplot(y='title', data=df, order=df['title'].value_counts().index, palette='prism')
sns.despine(bottom=False, left=True)
axes.set_ylim([9, 0])
axes.set_title('Overall 911 Emregency Calls', size=15)
axes.set(xlabel='Number of 911 Calls', ylabel='')
plt.tight_layout()


# In[12]:


df[df['reason']=='Traffic'].groupby('title_code').count()['lat'].sort_values(ascending=True).plot(kind='barh', figsize=(10, 5), color='darkblue')
plt.xlabel('Number of 911 Calls')
plt.ylabel('')
plt.title('Traffic 911 Emergency Calls', fontsize=15)


# In[13]:


df[df['reason']=='Fire'].groupby('title_code').count()['lat'].sort_values(ascending=True).tail(10).plot(kind='barh', figsize=(10, 5), color='darkred')
plt.xlabel('Number of 911 Calls')
plt.ylabel('')
plt.title('Fire 911 Emergency Calls', fontsize=15)


# In[14]:


df[df['reason']=='EMS'].groupby('title_code').count()['lat'].sort_values(ascending=True).tail(10).plot(kind='barh', figsize=(10, 5), color='darkgreen')
plt.xlabel('Number of 911 Calls')
plt.ylabel('')
plt.title('EMS 911 Emergency Calls', fontsize=15)


# In[15]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[16]:


# dictionary string names
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)


# In[17]:


fig, axes = plt.subplots(1,2, figsize=(15,5))

sns.countplot(x='Day of Week', data=df, palette='viridis', ax=axes[0])
axes[0].set_title('Weekly Calls', size=15)

sns.countplot(x='Month', data=df, hue='reason', palette='viridis', ax=axes[1])
axes[1].set_title('Monthly Calls', size=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

sns.despine(bottom=False, left=True)


# In[18]:


df['Date'] = df['timeStamp'].apply(lambda t: t.date())


# In[19]:


df[df['reason']=='Traffic'].groupby('Date').count()['lat'].plot(figsize=(15,5), color='darkblue')
plt.title('Traffic', fontsize=15)
sns.despine(bottom=False, left=True)
plt.tight_layout()


# In[20]:


df[df['reason']=='Fire'].groupby('Date').count()['lat'].plot(figsize=(15,5), color='darkred')
plt.title('Fire', fontsize=15)
sns.despine(bottom=False, left=True)
plt.tight_layout()


# In[21]:


df[df['reason']=='EMS'].groupby('Date').count()['lat'].plot(figsize=(15,5), color='darkgreen')
plt.title('EMS', fontsize=15)
sns.despine(bottom=False, left=True)
plt.tight_layout()


# In[22]:


dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['reason'].unstack()


# In[23]:



plt.figure(figsize=(12,6))
sns.heatmap(dayHour, cmap='viridis', linewidths=0.05)


# In[ ]:




