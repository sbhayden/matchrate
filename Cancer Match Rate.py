#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np

locations = pd.read_csv("patient_locations.csv") 
locations.head()


# In[2]:


bayer = pd.read_csv("BRCA1_BRCA2_ATM.csv")
bayer.head()


# In[3]:


bayer.count()


# In[4]:


incyte = pd.read_csv("FGFR.csv")
incyte.head()


# In[5]:


incyte.count()


# In[6]:


galahad = pd.read_csv("prostate.csv")
galahad.head()


# In[7]:


galahad.groupby(['Location'])


# In[8]:


locations = galahad.groupby('Location')
print(locations.groups)


# In[12]:


import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import point, polygon


# In[18]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))


# In[19]:


world.head()


# In[20]:


world.plot()


# In[22]:


gdf = gpd.locations(locations, geometry=gpd.points_from_xy(locations.longitude, locations.latitude))


# In[ ]:




