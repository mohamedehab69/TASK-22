#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':[8,8]},font_scale=1.4)


# In[2]:


df= sns.load_dataset('titanic')
df


# In[21]:


df.info()


# ### Numirical 

# **Univariate**

# In[3]:


sns.displot(df['age'],bins=30)


# In[4]:


sns.kdeplot(df['age'],shade=True)


# i noitced  the most ages between  20-40

# In[ ]:





# In[5]:


sns.displot(df['fare'],bins=30)


# In[6]:


sns.kdeplot(df['fare'],shade=True)


# i noticed the most people buy cheaper tickets

# **Bivarte**

# In[7]:


sns.jointplot(x='age',y='fare',data=df)


# i noticed  most people with different ages pay a little fare and there outlier pay a huge fare 

# ### Categorical

# **univariate**

# In[8]:


sns.countplot(df['survived'])


# Unfortunately i  noticed that most people did not survive

# In[9]:


sns.countplot(df['sex'])


# i noticed the most passengers are male

# In[10]:


sns.countplot(df['class'])


# i noticed most people take the third degree 

# In[11]:


sns.countplot(df['who'])


# i noticed the most passengers are men

# In[12]:


sns.countplot(df['embark_town'])


# the most passengers from southhampton

# In[13]:


sns.countplot(df['alive'])


# Unfortunately i noticed that most people did not survive

# In[14]:


sns.countplot(df['alone'])


# I noticed that most of the people were alone

# **bivariate**

# In[15]:


sns.boxplot(x='sex',y='survived',data=df)


# **i noticed the most survivor are female**

# In[16]:


sns.boxplot(x='who',y='survived',data=df)


# **i noticed the most survivor are child**

# In[35]:


sns.stripplot(x='who',y='fare',data=df,hue='sex')


# **i noticed the most people(child,woman,man) buy cheaper tickets**

# In[ ]:




