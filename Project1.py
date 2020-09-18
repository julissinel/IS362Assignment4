#!/usr/bin/env python
# coding: utf-8

# In[60]:


data=pd.read_csv("Project1.csv")


# In[61]:


data


# In[62]:


data = data.ffill(axis=0)


# In[64]:


data = data.set_index(['Flight','Status'])


# In[69]:


data.xs('delayed',level='Status')


# In[71]:


data


# In[77]:


new_data = data.xs('delayed',level='Status').T


# In[89]:


new_data


# In[88]:


new_data['Variance % in Delay']=((new_data.loc[:,'AM West'] - new_data.loc[:,'Alaska'])/new_data.loc[:,'AM West'])*100 


# In[90]:


new_data['Total Variance'] = new_data.loc[:,'AM West'] - new_data.loc[:,'Alaska']


# In[120]:


new_data = new_data.rename_axis(index=('Cities'))


# In[121]:


new_data.mean(axis=0)


# In[133]:


import matplotlib.pyplot as plt
new_data.plot(y=["Alaska","AM West"],kind="line",grid=True,marker="^")


# In[ ]:




