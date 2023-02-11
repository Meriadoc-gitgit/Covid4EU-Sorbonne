#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Import data
EfeILO = pd.read_csv("employ/EfeILO.csv")
EmaILO = pd.read_csv("employ/EmaILO.csv")

UfeILO = pd.read_csv("unemploy/UfeILO.csv")
UmaILO = pd.read_csv("unemploy/UmaILO.csv")


# ## Function to use later

# In[3]:


# Data building function
def built(data,numb,lst):
    lr = []
    for i in range(len(EfeILO)):
        if EfeILO["Country Name"][i] == lst[numb]:
            lr.append(data["2018"][i])
            lr.append(data["2019"][i])
            lr.append(data["2020"][i])
            lr.append(data["2021"][i])
    return lr


# In[138]:


def analyze(data):
    lr = []
    lr.append(0)
    for i in range(1,4):
        val = data[i] - data[i-1]
        lr.append(val)
    return lr


# In[139]:


# Define type array
type1_1 = ["France","Germany","United States","United Kingdom","Canada","Japan"]
type1_2 = ["Estonia","Latvia","Lithuania","Greece","Cyprus"]
type2_1 = ["Vietnam","Mexico","Brazil","Algeria","India","Russian Federation"]
type2_2 = ["Ukraine","Sri Lanka","Venezuela, RB","Nigeria","Colombia"]
type2_3 = ["Haiti","Madagascar","Burundi","Cambodia","Yemen, Rep."]


# ---

# In[140]:


# female
df11FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : analyze(built(EfeILO,0,type1_1)),
    "Germany" : analyze(built(EfeILO,1,type1_1)),
    "US" : analyze(built(EfeILO,2,type1_1)),
    "UK" : analyze(built(EfeILO,3,type1_1)),
    "Canada" : analyze(built(EfeILO,4,type1_1)),
    "Japan" : analyze(built(EfeILO,5,type1_1))
})
df11FE.set_index("",inplace=True)


# In[142]:


# male
df11ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : analyze(built(EmaILO,0,type1_1)),
    "Germany" : analyze(built(EmaILO,1,type1_1)),
    "US" : analyze(built(EmaILO,2,type1_1)),
    "UK" : analyze(built(EmaILO,3,type1_1)),
    "Canada" : analyze(built(EmaILO,4,type1_1)),
    "Japan" : analyze(built(EmaILO,5,type1_1))
})
df11ME.set_index("",inplace=True)


# ![type11_employ.png](attachment:type11_employ.png)

# In[143]:


df11ME


# In[144]:


df11FE


# ---

# In[145]:


# female
df11FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : analyze(built(UfeILO,0,type1_1)),
    "Germany" : analyze(built(UfeILO,1,type1_1)),
    "US" : analyze(built(UfeILO,2,type1_1)),
    "UK" : analyze(built(UfeILO,3,type1_1)),
    "Canada" : analyze(built(UfeILO,4,type1_1)),
    "Japan" : analyze(built(UfeILO,5,type1_1))
})
df11FU.set_index("",inplace=True)


# In[146]:



# male
df11MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : analyze(built(UmaILO,0,type1_1)),
    "Germany" : analyze(built(UmaILO,1,type1_1)),
    "US" : analyze(built(UmaILO,2,type1_1)),
    "UK" : analyze(built(UmaILO,3,type1_1)),
    "Canada" : analyze(built(UmaILO,4,type1_1)),
    "Japan" : analyze(built(UmaILO,5,type1_1))
})
df11MU.set_index("",inplace=True)


# ![type11_unemploy.png](attachment:type11_unemploy.png)

# In[147]:


df11FU


# In[148]:


df11MU


# ---

# In[149]:


# female
df12FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : analyze(built(EfeILO,0,type1_2)),
    "Latvia" : analyze(built(EfeILO,1,type1_2)),
    "Lithuania" : analyze(built(EfeILO,2,type1_2)),
    "Greece" : analyze(built(EfeILO,3,type1_2)),
    "Cyprus" : analyze(built(EfeILO,4,type1_2))
})
df12FE.set_index("",inplace=True)


# In[150]:


# male
df12ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : analyze(built(EmaILO,0,type1_2)),
    "Latvia" : analyze(built(EmaILO,1,type1_2)),
    "Lithuania" : analyze(built(EmaILO,2,type1_2)),
    "Greece" : analyze(built(EmaILO,3,type1_2)),
    "Cyprus" : analyze(built(EmaILO,4,type1_2)),
})
df12ME.set_index("",inplace=True)


# In[151]:


df12FE


# In[152]:


df12ME


# ---

# In[153]:


# female
df12FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : analyze(built(UfeILO,0,type1_2)),
    "Latvia" : analyze(built(UfeILO,1,type1_2)),
    "Lithuania" : analyze(built(UfeILO,2,type1_2)),
    "Greece" : analyze(built(UfeILO,3,type1_2)),
    "Cyprus" : analyze(built(UfeILO,4,type1_2)),
})
df12FU.set_index("",inplace=True)


# In[154]:


df12FU


# In[155]:


# male
df12MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : analyze(built(UmaILO,0,type1_2)),
    "Latvia" : analyze(built(UmaILO,1,type1_2)),
    "Lithuania" : analyze(built(UmaILO,2,type1_2)),
    "Greece" : analyze(built(UmaILO,3,type1_2)),
    "Cyprus" : analyze(built(UmaILO,4,type1_2)),
})
df12MU.set_index("",inplace=True)


# In[156]:


df12MU


# ---

# In[161]:


# female
df21FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : analyze(built(EfeILO,0,type2_1)),
    "Mexico" : analyze(built(EfeILO,1,type2_1)),
    "Brazil" : analyze(built(EfeILO,2,type2_1)),
    "Algeria" : analyze(built(EfeILO,3,type2_1)),
    "India" : analyze(built(EfeILO,4,type2_1)),
    "Russian Federation" : analyze(built(EfeILO,5,type2_1))
})
df21FE.set_index("",inplace=True)


# In[163]:


df21FE


# In[164]:


# male
df21ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : analyze(built(EmaILO,0,type2_1)),
    "Mexico" : analyze(built(EmaILO,1,type2_1)),
    "Brazil" : analyze(built(EmaILO,2,type2_1)),
    "Algeria" : analyze(built(EmaILO,3,type2_1)),
    "India" : analyze(built(EmaILO,4,type2_1)),
    "Russian Federation" : analyze(built(EmaILO,5,type2_1))
})
df21ME.set_index("",inplace=True)


# In[166]:


df21ME


# ---

# In[168]:


# female
df21FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : analyze(built(UfeILO,0,type2_1)),
    "Mexico" : analyze(built(UfeILO,1,type2_1)),
    "Brazil" : analyze(built(UfeILO,2,type2_1)),
    "Algeria" : analyze(built(UfeILO,3,type2_1)),
    "India" : analyze(built(UfeILO,4,type2_1)),
    "Russian Federation" : analyze(built(UfeILO,5,type2_1))
})
df21FU.set_index("",inplace=True)


# In[169]:


# male
df21MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : analyze(built(UmaILO,0,type2_1)),
    "Mexico" : analyze(built(UmaILO,1,type2_1)),
    "Brazil" : analyze(built(UmaILO,2,type2_1)),
    "Algeria" : analyze(built(UmaILO,3,type2_1)),
    "India" : analyze(built(UmaILO,4,type2_1)),
    "Russian Federation" : analyze(built(UmaILO,5,type2_1))
})
df21MU.set_index("",inplace=True)


# In[170]:


# female
df22FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : analyze(built(EfeILO,0,type2_2)),
    "Sri Lanka" : analyze(built(EfeILO,1,type2_2)),
    "Venezuela" : analyze(built(EfeILO,2,type2_2)),
    "Nigeria" : analyze(built(EfeILO,3,type2_2)),
    "Colombia" : analyze(built(EfeILO,4,type2_2)),
})
df22FE.set_index("",inplace=True)


# In[171]:


# male
df22ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : analyze(built(EmaILO,0,type2_2)),
    "Sri Lanka" : analyze(built(EmaILO,1,type2_2)),
    "Venezuela" : analyze(built(EmaILO,2,type2_2)),
    "Nigeria" : analyze(built(EmaILO,3,type2_2)),
    "Colombia" : analyze(built(EmaILO,4,type2_2)),
})
df22ME.set_index("",inplace=True)


# In[174]:


# female
df22FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : analyze(built(UfeILO,0,type2_2)),
    "Sri Lanka" : analyze(built(UfeILO,1,type2_2)),
    "Venezuela" : analyze(built(UfeILO,2,type2_2)),
    "Nigeria" : analyze(built(UfeILO,3,type2_2)),
    "Colombia" : analyze(built(UfeILO,4,type2_2)),
})
df22FU.set_index("",inplace=True)


# In[175]:


df22FU


# In[176]:


# male
df22MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : analyze(built(UmaILO,0,type2_2)),
    "Sri Lanka" : analyze(built(UmaILO,1,type2_2)),
    "Venezuela" : analyze(built(UmaILO,2,type2_2)),
    "Nigeria" : analyze(built(UmaILO,3,type2_2)),
    "Colombia" : analyze(built(UmaILO,4,type2_2)),
})
df22MU.set_index("",inplace=True)


# In[177]:


df22MU


# In[179]:


df23FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : analyze(built(EfeILO,0,type2_3)),
    "Madagascar" : analyze(built(EfeILO,1,type2_3)),
    "Burundi" : analyze(built(EfeILO,2,type2_3)),
    "Cambodia" : analyze(built(EfeILO,3,type2_3)),
    "Yemen" : analyze(built(EfeILO,4,type2_3)),
})
df23FE.set_index("",inplace=True)


# male
df23ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : analyze(built(EmaILO,0,type2_3)),
    "Madagascar" : analyze(built(EmaILO,1,type2_3)),
    "Burundi" : analyze(built(EmaILO,2,type2_3)),
    "Cambodia" : analyze(built(EmaILO,3,type2_3)),
    "Yemen" : analyze(built(EmaILO,4,type2_3)),
})
df23ME.set_index("",inplace=True)


# female
df23FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : analyze(built(UfeILO,0,type2_3)),
    "Madagascar" : analyze(built(UfeILO,1,type2_3)),
    "Burundi" : analyze(built(UfeILO,2,type2_3)),
    "Cambodia" : analyze(built(UfeILO,3,type2_3)),
    "Yemen" : analyze(built(UfeILO,4,type2_3)),
})
df23FU.set_index("",inplace=True)

# male
df23MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : analyze(built(UmaILO,0,type2_3)),
    "Madagascar" : analyze(built(UmaILO,1,type2_3)),
    "Burundi" : analyze(built(UmaILO,2,type2_3)),
    "Cambodia" : analyze(built(UmaILO,3,type2_3)),
    "Yemen" : analyze(built(UmaILO,4,type2_3)),
})
df23MU.set_index("",inplace=True)


# In[180]:


df11FE


# In[181]:


df11ME


# In[199]:


df23MU


# In[ ]:




