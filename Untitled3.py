#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import ast
import plotly.express as px
from plotly import graph_objects as go


# In[2]:


df = pd.read_csv("F:\Dataset1.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df["retail_price"].fillna(df["retail_price"].median(),inplace=True)
df["discounted_price"].fillna(df["discounted_price"].median(),inplace=True)


# In[5]:


x=df['retail_price']-df['discounted_price']
y=(x/df['retail_price'])*100
df['discount_percentage']=y


# In[11]:


df['main_category']=df['product_category_tree'].apply(lambda x :x.split('>>')[0][2:len(x.split('>>')[0])-1])


# In[12]:


n = 10
top_products=pd.DataFrame(df['main_category'].value_counts()  [:n]).reset_index()
top_products.rename(columns = {'index':'Top_Products','main_category':'Total_Count'}, inplace = True)


# In[15]:


from plotly.subplots import make_subplots #plotly library to create subplots

label1 = top_products['Top_Products']
value1=top_products['Total_Count']


# In[17]:


fig_both = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig_both.add_trace(go.Pie(labels=label1, values=value1, name="Top Products",pull=[0.3, 0, 0, 0]),
              1, 1)


# In[18]:


fig_both.update_traces(hole=.4, hoverinfo="label+percent+name")


# In[ ]:




