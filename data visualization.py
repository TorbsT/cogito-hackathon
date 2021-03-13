#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')



from sklearn.model_selection import train_test_split
from sklearn import mixture
from sklearn.mixture import GaussianMixture as GMM
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import metrics


# In[2]:


import zipfile
with zipfile.ZipFile('data/hackathon_kpis_anonymised.zip', 'r') as zip_ref:
    zip_ref.extractall('.')
    
df = pd.read_csv('hackathon_kpis_anonymised.csv')


# simple preproccessing

# In[3]:


df = df.sort_values(by = 'cell_name')
df = df.fillna(0.)
cell_occurrences = pd.DataFrame(df.cell_name.value_counts())
cell_occurrences.columns = ['count']


# In[4]:


df.head(n=8)


# In[ ]:




