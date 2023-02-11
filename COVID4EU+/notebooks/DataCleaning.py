#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Filter function

# In[38]:


def filterCountry(data):
    lst = ["Estonia","Latvia","Lithuania","Greece","Cyprus",
           "Vietnam","Mexico","Brazil","Algeria","India","Russian Federation",
           "Ukraine","Sri Lanka","Venezuela, RB","Nigeria","Colombia",
           "Haiti","Madagascar","Burundi","Cambodia","Yemen, Rep.",
           "France","Germany","United Kingdom","United States","Canada","Japan"]
    for i in range(len(data)):
        if data["Country Name"][i] not in lst:
            data.drop(i,axis=0,inplace=True)


# In[39]:


def cut(data):
    column = ["Country Name", "Country Code","2018","2019","2020","2021"]
    for i in np.array(data.columns):
        if i not in column:
            data.drop(i,axis=1,inplace=True)


# ---

# ### Employ 

# In[43]:


EfeILO = pd.read_csv("employ/female_modeledILO/main.csv")
Efenat = pd.read_csv("employ/female_national/main.csv")
EmaILO = pd.read_csv("employ/male_modeledILO/main.csv")
Emanat = pd.read_csv("employ/male_national/main.csv")

# Apply filter
filterCountry(EfeILO)
filterCountry(Efenat)
filterCountry(EmaILO)
filterCountry(Emanat)
# Cut data
cut(EfeILO)
cut(Efenat)
cut(EmaILO)
cut(Emanat)


# In[62]:


EfeILO.fillna(0,inplace=True)
EfeILO.to_csv("EfeILO.csv",index=False)
EfeILO = pd.read_csv("EfeILO.csv")
EfeILO


# In[61]:


Efenat.fillna(0,inplace=True)
Efenat.to_csv("Efenat.csv",index=False)
Efenat = pd.read_csv("Efenat.csv")
Efenat


# In[63]:


EmaILO.fillna(0,inplace=True)
EmaILO.to_csv("EmaILO.csv",index=False)
EmaILO = pd.read_csv("EmaILO.csv")
EmaILO


# In[64]:


Emanat.fillna(0,inplace=True)
Emanat.to_csv("Emanat.csv",index=False)
Emanat = pd.read_csv("Emanat.csv")
Emanat


# ---

# ### Unemployment 

# In[60]:


UfeILO = pd.read_csv("unemploy/female_ILO/main.csv")
Ufenat = pd.read_csv("unemploy/female_national/main.csv")
UmaILO = pd.read_csv("unemploy/male_ILO/main.csv")
Umanat = pd.read_csv("unemploy/male_national/main.csv")

# Apply filter
filterCountry(UfeILO)
filterCountry(Ufenat)
filterCountry(UmaILO)
filterCountry(Umanat)
# Cut data
cut(UfeILO)
cut(Ufenat)
cut(UmaILO)
cut(Umanat)


# In[65]:


UfeILO.fillna(0,inplace=True)
UfeILO.to_csv("UfeILO.csv",index=False)
UfeILO = pd.read_csv("UfeILO.csv")

Ufenat.fillna(0,inplace=True)
Ufenat.to_csv("Ufenat.csv",index=False)
Ufenat = pd.read_csv("Ufenat.csv")

UmaILO.fillna(0,inplace=True)
UmaILO.to_csv("UmaILO.csv",index=False)
UmaILO = pd.read_csv("UmaILO.csv")

Umanat.fillna(0,inplace=True)
Umanat.to_csv("Umanat.csv",index=False)
Umanat = pd.read_csv("Umanat.csv")


# ---
