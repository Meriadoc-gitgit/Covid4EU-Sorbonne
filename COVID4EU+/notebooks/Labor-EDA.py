#!/usr/bin/env python
# coding: utf-8

# Works by Vu Hoang-Thuy-Duong

# In[1]:


# Import necessary libraries
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


# ---

# We are interested in 2 categories: **Developped** countries and **Developping** countries
# 1. *Developped* countries:
# In this part, we divide countries taken into 2 types:
# - Rich and industrialized countries, head of GDP classement: **France, Germany, UK, USA, Canada, Japan**
# - Developped countries who just finish the process of industralization: **Estonia, Latvia, Lithuania, Greece, Cyprus**
# 2. *Developping* countries: 
# And in this part, we divide countries taken into 3 types:
# - who has a stable economic growth: **Vietnam, Mexico, Brazil, Algeria, India, Russian Federation**
# - who has an unstable economic growth due to politic situation: **Ukraine, Sri Lanka, Venezuela, Nigeria, Colombia**
# - the less developping than all other types (PMA via ONU): **Haiti, Madagascar, Burundi, Cambodia, Yemen**

# In[4]:


# Define type array
type1_1 = ["France","Germany","United States","United Kingdom","Canada","Japan"]
type1_2 = ["Estonia","Latvia","Lithuania","Greece","Cyprus"]
type2_1 = ["Vietnam","Mexico","Brazil","Algeria","India","Russian Federation"]
type2_2 = ["Ukraine","Sri Lanka","Venezuela, RB","Nigeria","Colombia"]
type2_3 = ["Haiti","Madagascar","Burundi","Cambodia","Yemen, Rep."]


# ## Plot

# In[5]:


fig, ax = plt.subplots(2,3)
fig.set_size_inches(20, 12, forward = True) # modifier la taille de la figure
fig.suptitle("Developped countries T1.1 Employment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df11FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : built(EfeILO,0,type1_1),
    "Germany" : built(EfeILO,1,type1_1),
    "US" : built(EfeILO,2,type1_1),
    "UK" : built(EfeILO,3,type1_1),
    "Canada" : built(EfeILO,4,type1_1),
    "Japan" : built(EfeILO,5,type1_1)
})
df11FE.set_index("",inplace=True)

# male
df11ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : built(EmaILO,0,type1_1),
    "Germany" : built(EmaILO,1,type1_1),
    "US" : built(EmaILO,2,type1_1),
    "UK" : built(EmaILO,3,type1_1),
    "Canada" : built(EmaILO,4,type1_1),
    "Japan" : built(EmaILO,5,type1_1)
})
df11ME.set_index("",inplace=True)

# plot
ax[0,0].plot(df11FE["France"],color="pink",marker=".",label="Female")
ax[0,0].plot(df11ME["France"],color="red",marker=".",label="Male")

ax[0,1].plot(df11FE["Germany"],color="skyblue",marker=".",label="Female")
ax[0,1].plot(df11ME["Germany"],color="blue",marker=".",label="Male")

ax[0,2].plot(df11FE["US"],color="plum",marker=".",label="Female")
ax[0,2].plot(df11ME["US"],color="purple",marker=".",label="Male")

ax[1,0].plot(df11FE["UK"],color="yellowgreen",marker=".",label="Female")
ax[1,0].plot(df11ME["UK"],color="green",marker=".",label="Male")

ax[1,1].plot(df11FE["Canada"],color="wheat",marker=".",label="Female")
ax[1,1].plot(df11ME["Canada"],color="orange",marker=".",label="Male")

ax[1,2].plot(df11FE["Japan"],color="slategrey",marker=".",label="Female")
ax[1,2].plot(df11ME["Japan"],color="black",marker=".",label="Male")

ax[0,0].legend(loc='center')
ax[0,1].legend(loc='center')
ax[0,2].legend(loc='center')
ax[1,0].legend(loc='center')
ax[1,1].legend(loc='center')
ax[1,2].legend(loc='center')

ax[0,0].set_xlabel("France",fontsize=12)
ax[0,1].set_xlabel("Germany",fontsize=12)
ax[0,2].set_xlabel("United States",fontsize=12)
ax[1,0].set_xlabel("United Kingdom",fontsize=12)
ax[1,1].set_xlabel("Canada",fontsize=12)
ax[1,2].set_xlabel("Japan",fontsize=12)

plt.savefig("type11_employ.png")


# In[6]:


fig, ax = plt.subplots(2,3)
fig.set_size_inches(20, 12, forward = True) # modifier la taille de la figure
fig.suptitle("Developped countries T1.1 Unemployment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df11FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : built(UfeILO,0,type1_1),
    "Germany" : built(UfeILO,1,type1_1),
    "US" : built(UfeILO,2,type1_1),
    "UK" : built(UfeILO,3,type1_1),
    "Canada" : built(UfeILO,4,type1_1),
    "Japan" : built(UfeILO,5,type1_1)
})
df11FU.set_index("",inplace=True)

# male
df11MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "France" : built(UmaILO,0,type1_1),
    "Germany" : built(UmaILO,1,type1_1),
    "US" : built(UmaILO,2,type1_1),
    "UK" : built(UmaILO,3,type1_1),
    "Canada" : built(UmaILO,4,type1_1),
    "Japan" : built(UmaILO,5,type1_1)
})
df11MU.set_index("",inplace=True)

# plot
ax[0,0].plot(df11FU["France"],color="pink",marker=".",label="Female")
ax[0,0].plot(df11MU["France"],color="red",marker=".",label="Male")

ax[0,1].plot(df11FU["Germany"],color="skyblue",marker=".",label="Female")
ax[0,1].plot(df11MU["Germany"],color="blue",marker=".",label="Male")

ax[0,2].plot(df11FU["US"],color="plum",marker=".",label="Female")
ax[0,2].plot(df11MU["US"],color="purple",marker=".",label="Male")

ax[1,0].plot(df11FU["UK"],color="yellowgreen",marker=".",label="Female")
ax[1,0].plot(df11MU["UK"],color="green",marker=".",label="Male")

ax[1,1].plot(df11FU["Canada"],color="wheat",marker=".",label="Female")
ax[1,1].plot(df11MU["Canada"],color="orange",marker=".",label="Male")

ax[1,2].plot(df11FU["Japan"],color="slategrey",marker=".",label="Female")
ax[1,2].plot(df11MU["Japan"],color="black",marker=".",label="Male")

ax[0,0].legend(loc='upper right')
ax[0,1].legend(loc='upper left')
ax[0,2].legend(loc='upper left')
ax[1,0].legend(loc='upper left')
ax[1,1].legend(loc='upper left')
ax[1,2].legend(loc='upper left')

ax[0,0].set_xlabel("France",fontsize=12)
ax[0,1].set_xlabel("Germany",fontsize=12)
ax[0,2].set_xlabel("United States",fontsize=12)
ax[1,0].set_xlabel("United Kingdom",fontsize=12)
ax[1,1].set_xlabel("Canada",fontsize=12)
ax[1,2].set_xlabel("Japan",fontsize=12)

plt.savefig("type11_unemploy.png")


# In[7]:


df11FU


# ---

# In[8]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developped countries T1.2 Employment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df12FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : built(EfeILO,0,type1_2),
    "Latvia" : built(EfeILO,1,type1_2),
    "Lithuania" : built(EfeILO,2,type1_2),
    "Greece" : built(EfeILO,3,type1_2),
    "Cyprus" : built(EfeILO,4,type1_2),
})
df12FE.set_index("",inplace=True)

# male
df12ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : built(EmaILO,0,type1_2),
    "Latvia" : built(EmaILO,1,type1_2),
    "Lithuania" : built(EmaILO,2,type1_2),
    "Greece" : built(EmaILO,3,type1_2),
    "Cyprus" : built(EmaILO,4,type1_2),
})
df12ME.set_index("",inplace=True)

# plot
ax[0].plot(df12FE["Estonia"],color="pink",marker=".",label="Female")
ax[0].plot(df12ME["Estonia"],color="red",marker=".",label="Male")

ax[1].plot(df12FE["Latvia"],color="skyblue",marker=".",label="Female")
ax[1].plot(df12ME["Latvia"],color="blue",marker=".",label="Male")

ax[2].plot(df12FE["Lithuania"],color="plum",marker=".",label="Female")
ax[2].plot(df12ME["Lithuania"],color="purple",marker=".",label="Male")

ax[3].plot(df12FE["Greece"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df12ME["Greece"],color="green",marker=".",label="Male")

ax[4].plot(df12FE["Cyprus"],color="wheat",marker=".",label="Female")
ax[4].plot(df12ME["Cyprus"],color="orange",marker=".",label="Male")

ax[0].legend(loc='center')
ax[1].legend(loc='center')
ax[2].legend(loc='center')
ax[3].legend(loc='center')
ax[4].legend(loc='center')

ax[0].set_xlabel("Estonia",fontsize=12)
ax[1].set_xlabel("Latvia",fontsize=12)
ax[2].set_xlabel("Lithuania",fontsize=12)
ax[3].set_xlabel("Greece",fontsize=12)
ax[4].set_xlabel("Cyprus",fontsize=12)

plt.savefig("type12_employ.png")


# In[9]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developped countries T1.2 Unemployment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df12FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : built(UfeILO,0,type1_2),
    "Latvia" : built(UfeILO,1,type1_2),
    "Lithuania" : built(UfeILO,2,type1_2),
    "Greece" : built(UfeILO,3,type1_2),
    "Cyprus" : built(UfeILO,4,type1_2),
})
df12FU.set_index("",inplace=True)

# male
df12MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Estonia" : built(UmaILO,0,type1_2),
    "Latvia" : built(UmaILO,1,type1_2),
    "Lithuania" : built(UmaILO,2,type1_2),
    "Greece" : built(UmaILO,3,type1_2),
    "Cyprus" : built(UmaILO,4,type1_2),
})
df12MU.set_index("",inplace=True)

# plot
ax[0].plot(df12FU["Estonia"],color="pink",marker=".",label="Female")
ax[0].plot(df12MU["Estonia"],color="red",marker=".",label="Male")

ax[1].plot(df12FU["Latvia"],color="skyblue",marker=".",label="Female")
ax[1].plot(df12MU["Latvia"],color="blue",marker=".",label="Male")

ax[2].plot(df12FU["Lithuania"],color="plum",marker=".",label="Female")
ax[2].plot(df12MU["Lithuania"],color="purple",marker=".",label="Male")

ax[3].plot(df12FU["Greece"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df12MU["Greece"],color="green",marker=".",label="Male")

ax[4].plot(df12FU["Cyprus"],color="wheat",marker=".",label="Female")
ax[4].plot(df12MU["Cyprus"],color="orange",marker=".",label="Male")

ax[0].legend(loc='upper left')
ax[1].legend(loc='upper left')
ax[2].legend(loc='upper left')
ax[3].legend(loc='upper right')
ax[4].legend(loc='upper right')

ax[0].set_xlabel("Estonia",fontsize=12)
ax[1].set_xlabel("Latvia",fontsize=12)
ax[2].set_xlabel("Lithuania",fontsize=12)
ax[3].set_xlabel("Greece",fontsize=12)
ax[4].set_xlabel("Cyprus",fontsize=12)

plt.savefig("type12_unemploy.png")


# ---

# In[10]:


fig, ax = plt.subplots(2,3)
fig.set_size_inches(20, 12, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.1 Employment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df21FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : built(EfeILO,0,type2_1),
    "Mexico" : built(EfeILO,1,type2_1),
    "Brazil" : built(EfeILO,2,type2_1),
    "Algeria" : built(EfeILO,3,type2_1),
    "India" : built(EfeILO,4,type2_1),
    "Russian Federation" : built(EfeILO,5,type2_1)
})
df21FE.set_index("",inplace=True)

# male
df21ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : built(EmaILO,0,type2_1),
    "Mexico" : built(EmaILO,1,type2_1),
    "Brazil" : built(EmaILO,2,type2_1),
    "Algeria" : built(EmaILO,3,type2_1),
    "India" : built(EmaILO,4,type2_1),
    "Russian Federation" : built(EmaILO,5,type2_1)
})
df21ME.set_index("",inplace=True)

# plot
ax[0,0].plot(df21FE["Vietnam"],color="pink",marker=".",label="Female")
ax[0,0].plot(df21ME["Vietnam"],color="red",marker=".",label="Male")

ax[0,1].plot(df21FE["Mexico"],color="skyblue",marker=".",label="Female")
ax[0,1].plot(df21ME["Mexico"],color="blue",marker=".",label="Male")

ax[0,2].plot(df21FE["Brazil"],color="plum",marker=".",label="Female")
ax[0,2].plot(df21ME["Brazil"],color="purple",marker=".",label="Male")

ax[1,0].plot(df21FE["Algeria"],color="yellowgreen",marker=".",label="Female")
ax[1,0].plot(df21ME["Algeria"],color="green",marker=".",label="Male")

ax[1,1].plot(df21FE["India"],color="wheat",marker=".",label="Female")
ax[1,1].plot(df21ME["India"],color="orange",marker=".",label="Male")

ax[1,2].plot(df21FE["Russian Federation"],color="slategrey",marker=".",label="Female")
ax[1,2].plot(df21ME["Russian Federation"],color="black",marker=".",label="Male")

ax[0,0].legend(loc='center')
ax[0,1].legend(loc='center')
ax[0,2].legend(loc='center')
ax[1,0].legend(loc='center')
ax[1,1].legend(loc='center')
ax[1,2].legend(loc='center')

ax[0,0].set_xlabel("Vietnam",fontsize=12)
ax[0,1].set_xlabel("Mexico",fontsize=12)
ax[0,2].set_xlabel("Brazil",fontsize=12)
ax[1,0].set_xlabel("Algeria",fontsize=12)
ax[1,1].set_xlabel("India",fontsize=12)
ax[1,2].set_xlabel("Russian Federation",fontsize=12)

plt.savefig("type21_employ.png")


# In[11]:


fig, ax = plt.subplots(2,3)
fig.set_size_inches(20, 12, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.1 Unemployment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df21FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : built(UfeILO,0,type2_1),
    "Mexico" : built(UfeILO,1,type2_1),
    "Brazil" : built(UfeILO,2,type2_1),
    "Algeria" : built(UfeILO,3,type2_1),
    "India" : built(UfeILO,4,type2_1),
    "Russian Federation" : built(UfeILO,5,type2_1)
})
df21FU.set_index("",inplace=True)

# male
df21MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Vietnam" : built(UmaILO,0,type2_1),
    "Mexico" : built(UmaILO,1,type2_1),
    "Brazil" : built(UmaILO,2,type2_1),
    "Algeria" : built(UmaILO,3,type2_1),
    "India" : built(UmaILO,4,type2_1),
    "Russian Federation" : built(UmaILO,5,type2_1)
})
df21MU.set_index("",inplace=True)

# plot
ax[0,0].plot(df21FU["Vietnam"],color="pink",marker=".",label="Female")
ax[0,0].plot(df21MU["Vietnam"],color="red",marker=".",label="Male")

ax[0,1].plot(df21FU["Mexico"],color="skyblue",marker=".",label="Female")
ax[0,1].plot(df21MU["Mexico"],color="blue",marker=".",label="Male")

ax[0,2].plot(df21FU["Brazil"],color="plum",marker=".",label="Female")
ax[0,2].plot(df21MU["Brazil"],color="purple",marker=".",label="Male")

ax[1,0].plot(df21FU["Algeria"],color="yellowgreen",marker=".",label="Female")
ax[1,0].plot(df21MU["Algeria"],color="green",marker=".",label="Male")

ax[1,1].plot(df21FU["India"],color="wheat",marker=".",label="Female")
ax[1,1].plot(df21MU["India"],color="orange",marker=".",label="Male")

ax[1,2].plot(df21FU["Russian Federation"],color="slategrey",marker=".",label="Female")
ax[1,2].plot(df21MU["Russian Federation"],color="black",marker=".",label="Male")

ax[0,0].legend(loc='upper left')
ax[0,1].legend(loc='upper left')
ax[0,2].legend(loc='upper left')
ax[1,0].legend(loc='center')
ax[1,1].legend(loc='upper left')
ax[1,2].legend(loc='upper left')

ax[0,0].set_xlabel("Vietnam",fontsize=12)
ax[0,1].set_xlabel("Mexico",fontsize=12)
ax[0,2].set_xlabel("Brazil",fontsize=12)
ax[1,0].set_xlabel("Algeria",fontsize=12)
ax[1,1].set_xlabel("India",fontsize=12)
ax[1,2].set_xlabel("Russian Federation",fontsize=12)

plt.savefig("type21_unemploy.png")


# ---

# In[12]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.2 Employment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df22FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : built(EfeILO,0,type2_2),
    "Sri Lanka" : built(EfeILO,1,type2_2),
    "Venezuela" : built(EfeILO,2,type2_2),
    "Nigeria" : built(EfeILO,3,type2_2),
    "Colombia" : built(EfeILO,4,type2_2),
})
df22FE.set_index("",inplace=True)

# male
df22ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : built(EmaILO,0,type2_2),
    "Sri Lanka" : built(EmaILO,1,type2_2),
    "Venezuela" : built(EmaILO,2,type2_2),
    "Nigeria" : built(EmaILO,3,type2_2),
    "Colombia" : built(EmaILO,4,type2_2),
})
df22ME.set_index("",inplace=True)

# plot
ax[0].plot(df22FE["Ukraine"],color="pink",marker=".",label="Female")
ax[0].plot(df22ME["Ukraine"],color="red",marker=".",label="Male")

ax[1].plot(df22FE["Sri Lanka"],color="skyblue",marker=".",label="Female")
ax[1].plot(df22ME["Sri Lanka"],color="blue",marker=".",label="Male")

ax[2].plot(df22FE["Venezuela"],color="plum",marker=".",label="Female")
ax[2].plot(df22ME["Venezuela"],color="purple",marker=".",label="Male")

ax[3].plot(df22FE["Nigeria"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df22ME["Nigeria"],color="green",marker=".",label="Male")

ax[4].plot(df22FE["Colombia"],color="wheat",marker=".",label="Female")
ax[4].plot(df22ME["Colombia"],color="orange",marker=".",label="Male")

ax[0].legend(loc='center')
ax[1].legend(loc='center')
ax[2].legend(loc='center')
ax[3].legend(loc='center')
ax[4].legend(loc='center')

ax[0].set_xlabel("Ukraine",fontsize=12)
ax[1].set_xlabel("Sri Lanka",fontsize=12)
ax[2].set_xlabel("Venezuela",fontsize=12)
ax[3].set_xlabel("Nigeria",fontsize=12)
ax[4].set_xlabel("Colombia",fontsize=12)

plt.savefig("type22_employ.png")


# In[13]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.2 Unemployment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df22FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : built(UfeILO,0,type2_2),
    "Sri Lanka" : built(UfeILO,1,type2_2),
    "Venezuela" : built(UfeILO,2,type2_2),
    "Nigeria" : built(UfeILO,3,type2_2),
    "Colombia" : built(UfeILO,4,type2_2),
})
df22FU.set_index("",inplace=True)

# male
df22MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Ukraine" : built(UmaILO,0,type2_2),
    "Sri Lanka" : built(UmaILO,1,type2_2),
    "Venezuela" : built(UmaILO,2,type2_2),
    "Nigeria" : built(UmaILO,3,type2_2),
    "Colombia" : built(UmaILO,4,type2_2),
})
df22MU.set_index("",inplace=True)

# plot
ax[0].plot(df22FU["Ukraine"],color="pink",marker=".",label="Female")
ax[0].plot(df22MU["Ukraine"],color="red",marker=".",label="Male")

ax[1].plot(df22FU["Sri Lanka"],color="skyblue",marker=".",label="Female")
ax[1].plot(df22MU["Sri Lanka"],color="blue",marker=".",label="Male")

ax[2].plot(df22FU["Venezuela"],color="plum",marker=".",label="Female")
ax[2].plot(df22MU["Venezuela"],color="purple",marker=".",label="Male")

ax[3].plot(df22FU["Nigeria"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df22MU["Nigeria"],color="green",marker=".",label="Male")

ax[4].plot(df22FU["Colombia"],color="wheat",marker=".",label="Female")
ax[4].plot(df22MU["Colombia"],color="orange",marker=".",label="Male")

ax[0].legend(loc='upper right')
ax[1].legend(loc='upper left')
ax[2].legend(loc='upper left')
ax[3].legend(loc='upper left')
ax[4].legend(loc='upper left')

ax[0].set_xlabel("Ukraine",fontsize=12)
ax[1].set_xlabel("Sri Lanka",fontsize=12)
ax[2].set_xlabel("Venezuela",fontsize=12)
ax[3].set_xlabel("Nigeria",fontsize=12)
ax[4].set_xlabel("Colombia",fontsize=12)

plt.savefig("type22_unemploy.png")


# ---

# In[14]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.3 Employment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df23FE = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : built(EfeILO,0,type2_3),
    "Madagascar" : built(EfeILO,1,type2_3),
    "Burundi" : built(EfeILO,2,type2_3),
    "Cambodia" : built(EfeILO,3,type2_3),
    "Yemen" : built(EfeILO,4,type2_3),
})
df23FE.set_index("",inplace=True)

# male
df23ME = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : built(EmaILO,0,type2_3),
    "Madagascar" : built(EmaILO,1,type2_3),
    "Burundi" : built(EmaILO,2,type2_3),
    "Cambodia" : built(EmaILO,3,type2_3),
    "Yemen" : built(EmaILO,4,type2_3),
})
df23ME.set_index("",inplace=True)

# plot
ax[0].plot(df23FE["Haiti"],color="pink",marker=".",label="Female")
ax[0].plot(df23ME["Haiti"],color="red",marker=".",label="Male")

ax[1].plot(df23FE["Madagascar"],color="skyblue",marker=".",label="Female")
ax[1].plot(df23ME["Madagascar"],color="blue",marker=".",label="Male")

ax[2].plot(df23FE["Burundi"],color="plum",marker=".",label="Female")
ax[2].plot(df23ME["Burundi"],color="purple",marker=".",label="Male")

ax[3].plot(df23FE["Cambodia"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df23ME["Cambodia"],color="green",marker=".",label="Male")

ax[4].plot(df23FE["Yemen"],color="wheat",marker=".",label="Female")
ax[4].plot(df23ME["Yemen"],color="orange",marker=".",label="Male")

ax[0].legend(loc='center')
ax[1].legend(loc='center')
ax[2].legend(loc='center')
ax[3].legend(loc='center')
ax[4].legend(loc='center')

ax[0].set_xlabel("Haiti",fontsize=12)
ax[1].set_xlabel("Madagascar",fontsize=12)
ax[2].set_xlabel("Burundi",fontsize=12)
ax[3].set_xlabel("Cambodia",fontsize=12)
ax[4].set_xlabel("Yemen",fontsize=12)

plt.savefig("type23_employ.png")


# In[15]:


fig, ax = plt.subplots(1,5)
fig.set_size_inches(35,7, forward = True) # modifier la taille de la figure
fig.suptitle("Developping countries T2.3 Unemployment rate of men and women 2018-2021", fontsize = 14.5)

# Build a DataFrame

# female
df23FU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : built(UfeILO,0,type2_3),
    "Madagascar" : built(UfeILO,1,type2_3),
    "Burundi" : built(UfeILO,2,type2_3),
    "Cambodia" : built(UfeILO,3,type2_3),
    "Yemen" : built(UfeILO,4,type2_3),
})
df23FU.set_index("",inplace=True)

# male
df23MU = pd.DataFrame({
    "" : ["2018","2019","2020","2021"],
    "Haiti" : built(UmaILO,0,type2_3),
    "Madagascar" : built(UmaILO,1,type2_3),
    "Burundi" : built(UmaILO,2,type2_3),
    "Cambodia" : built(UmaILO,3,type2_3),
    "Yemen" : built(UmaILO,4,type2_3),
})
df23MU.set_index("",inplace=True)

# plot
ax[0].plot(df23FU["Haiti"],color="pink",marker=".",label="Female")
ax[0].plot(df23MU["Haiti"],color="red",marker=".",label="Male")

ax[1].plot(df23FU["Madagascar"],color="skyblue",marker=".",label="Female")
ax[1].plot(df23MU["Madagascar"],color="blue",marker=".",label="Male")

ax[2].plot(df23FU["Burundi"],color="plum",marker=".",label="Female")
ax[2].plot(df23MU["Burundi"],color="purple",marker=".",label="Male")

ax[3].plot(df23FU["Cambodia"],color="yellowgreen",marker=".",label="Female")
ax[3].plot(df23MU["Cambodia"],color="green",marker=".",label="Male")

ax[4].plot(df23FU["Yemen"],color="wheat",marker=".",label="Female")
ax[4].plot(df23MU["Yemen"],color="orange",marker=".",label="Male")

ax[0].legend(loc='upper left')
ax[1].legend(loc='upper left')
ax[2].legend(loc='center')
ax[3].legend(loc='upper left')
ax[4].legend(loc='center')

ax[0].set_xlabel("Haiti",fontsize=12)
ax[1].set_xlabel("Madagascar",fontsize=12)
ax[2].set_xlabel("Burundi",fontsize=12)
ax[3].set_xlabel("Cambodia",fontsize=12)
ax[4].set_xlabel("Yemen",fontsize=12)

plt.savefig("type23_unemploy.png")


# ---

# ## Bar

# In[16]:


type1_2


# In[21]:


fig, ax = plt.subplots(3,4)
fig.set_size_inches(40,20, forward = True)
fig.suptitle("Developped countries T1.1 Labor decisions of men and women 2018-2021", fontsize = 14.5)

lst1=[1,1,1,1]
lst2=[2,2,2,2]

year=["2018","2019","2020","2021"]

ax[0,0].bar(year,df11FE["France"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,0].bar(year,df11ME["France"],0.25,label="Men",bottom=df11FE["France"],yerr=lst2,color="pink")
ax[0,0].set_title("France - Employment force",fontsize=12)
ax[0,0].legend(loc="lower center")

ax[0,1].bar(year,df11FU["France"],0.25,yerr=lst1,label="Women",color="orange")
ax[0,1].bar(year,df11MU["France"],0.25,label="Men",bottom=df11FU["France"],yerr=lst1,color="wheat")
ax[0,1].set_title("France - Unemployment force",fontsize=12)
ax[0,1].legend(loc="lower center")

ax[0,2].bar(year,df11FE["Germany"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,2].bar(year,df11ME["Germany"],0.25,label="Men",bottom=df11FE["Germany"],yerr=lst2,color="pink")
ax[0,2].set_title("Germany - Employment force",fontsize=12)
ax[0,2].legend(loc="lower center")

ax[0,3].bar(year,df11FU["Germany"],0.25,yerr=lst1,label="Women",color="orange")
ax[0,3].bar(year,df11MU["Germany"],0.25,label="Men",bottom=df11FU["Germany"],yerr=lst1,color="wheat")
ax[0,3].set_title("Germany - Unemployment force",fontsize=12)
ax[0,3].legend(loc="lower center")

ax[1,0].bar(year,df11FE["US"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[1,0].bar(year,df11ME["US"],0.25,label="Men",bottom=df11FE["US"],yerr=lst2,color="pink")
ax[1,0].set_title("United States - Employment force",fontsize=12)
ax[1,0].legend(loc="lower center")

ax[1,1].bar(year,df11FU["US"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,1].bar(year,df11MU["US"],0.25,label="Men",bottom=df11FU["US"],yerr=lst1,color="wheat")
ax[1,1].set_title("United States - Unemployment force",fontsize=12)
ax[1,1].legend(loc="lower center")

ax[1,2].bar(year,df11FE["UK"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[1,2].bar(year,df11ME["UK"],0.25,label="Men",bottom=df11FE["UK"],yerr=lst2,color="pink")
ax[1,2].set_title("United Kingdom - Employment force",fontsize=12)
ax[1,2].legend(loc="lower center")

ax[1,3].bar(year,df11FU["UK"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,3].bar(year,df11MU["UK"],0.25,label="Men",bottom=df11FU["UK"],yerr=lst1,color="wheat")
ax[1,3].set_title("United Kingdom - Unemployment force",fontsize=12)
ax[1,3].legend(loc="lower center")

ax[2,0].bar(year,df11FE["Canada"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[2,0].bar(year,df11ME["Canada"],0.25,label="Men",bottom=df11FE["Canada"],yerr=lst2,color="pink")
ax[2,0].set_title("Canada - Employment force",fontsize=12)
ax[2,0].legend(loc="lower center")

ax[2,1].bar(year,df11FU["Canada"],0.25,yerr=lst1,label="Women",color="orange")
ax[2,1].bar(year,df11MU["Canada"],0.25,label="Men",bottom=df11FU["Canada"],yerr=lst1,color="wheat")
ax[2,1].set_title("Canada - Unemployment force",fontsize=12)
ax[2,1].legend(loc="lower center")

ax[2,2].bar(year,df11FE["Japan"],0.25,yerr=[2,2,2,2],label="Women",color="skyblue")
ax[2,2].bar(year,df11ME["Japan"],0.25,label="Men",bottom=df11FE["Japan"],yerr=[2,2,2,2],color="pink")
ax[2,2].set_title("Japan - Employment force",fontsize=12)
ax[2,2].legend(loc="lower center")

ax[2,3].bar(year,df11FU["Japan"],0.25,yerr=lst1,label="Women",color="orange")
ax[2,3].bar(year,df11MU["Japan"],0.25,label="Men",bottom=df11FU["Japan"],yerr=lst1,color="wheat")
ax[2,3].set_title("Japan - Unemployment force",fontsize=12)
ax[2,3].legend(loc="lower center")

plt.savefig("labort11.png")


# In[22]:


fig, ax = plt.subplots(2,5)
fig.set_size_inches(40,20, forward = True)
fig.suptitle("Developped countries T1.2 Labor decisions of men and women 2018-2021", fontsize = 14.5)

lst1=[1,1,1,1]
lst2=[2,2,2,2]

year=["2018","2019","2020","2021"]

ax[0,0].bar(year,df12FE["Estonia"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,0].bar(year,df12ME["Estonia"],0.25,label="Men",bottom=df12FE["Estonia"],yerr=lst2,color="pink")
ax[0,0].set_title("Estonia - Employment force",fontsize=12)
ax[0,0].legend(loc="lower center")

ax[1,0].bar(year,df12FU["Estonia"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,0].bar(year,df12MU["Estonia"],0.25,label="Men",bottom=df12FU["Estonia"],yerr=lst1,color="wheat")
ax[1,0].set_title("Estonia - Unemployment force",fontsize=12)
ax[1,0].legend(loc="lower center")

ax[0,1].bar(year,df12FE["Latvia"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,1].bar(year,df12ME["Latvia"],0.25,label="Men",bottom=df12FE["Latvia"],yerr=lst2,color="pink")
ax[0,1].set_title("Latvia - Employment force",fontsize=12)
ax[0,1].legend(loc="lower center")

ax[1,1].bar(year,df12FU["Latvia"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,1].bar(year,df12MU["Latvia"],0.25,label="Men",bottom=df12FU["Latvia"],yerr=lst1,color="wheat")
ax[1,1].set_title("Latvia - Unemployment force",fontsize=12)
ax[1,1].legend(loc="lower center")

ax[0,2].bar(year,df12FE["Lithuania"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,2].bar(year,df12ME["Lithuania"],0.25,label="Men",bottom=df12FE["Lithuania"],yerr=lst2,color="pink")
ax[0,2].set_title("Lithuania - Employment force",fontsize=12)
ax[0,2].legend(loc="lower center")

ax[1,2].bar(year,df12FU["Lithuania"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,2].bar(year,df12MU["Lithuania"],0.25,label="Men",bottom=df12FU["Lithuania"],yerr=lst1,color="wheat")
ax[1,2].set_title("Lithuania - Unemployment force",fontsize=12)
ax[1,2].legend(loc="lower center")

ax[0,3].bar(year,df12FE["Greece"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,3].bar(year,df12ME["Greece"],0.25,label="Men",bottom=df12FE["Greece"],yerr=lst2,color="pink")
ax[0,3].set_title("Greece - Employment force",fontsize=12)
ax[0,3].legend(loc="lower center")

ax[1,3].bar(year,df12FU["Greece"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,3].bar(year,df12MU["Greece"],0.25,label="Men",bottom=df12FU["Greece"],yerr=lst1,color="wheat")
ax[1,3].set_title("Greece - Unemployment force",fontsize=12)
ax[1,3].legend(loc="lower center")

ax[0,4].bar(year,df12FE["Cyprus"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,4].bar(year,df12ME["Cyprus"],0.25,label="Men",bottom=df12FE["Cyprus"],yerr=lst2,color="pink")
ax[0,4].set_title("Cyprus - Employment force",fontsize=12)
ax[0,4].legend(loc="lower center")

ax[1,4].bar(year,df12FU["Cyprus"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,4].bar(year,df12MU["Cyprus"],0.25,label="Men",bottom=df12FU["Cyprus"],yerr=lst1,color="wheat")
ax[1,4].set_title("Cyprus - Unemployment force",fontsize=12)
ax[1,4].legend(loc="lower center")

plt.savefig("labort12.png")


# In[254]:


type2_2


# In[23]:


fig, ax = plt.subplots(3,4)
fig.set_size_inches(40,20, forward = True)
fig.suptitle("Developped countries T2.1 Labor decisions of men and women 2018-2021", fontsize = 14.5)

lst1=[1,1,1,1]
lst2=[2,2,2,2]

year=["2018","2019","2020","2021"]

ax[0,0].bar(year,df21FE["Vietnam"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,0].bar(year,df21ME["Vietnam"],0.25,label="Men",bottom=df21FE["Vietnam"],yerr=lst2,color="pink")
ax[0,0].set_title("Vietnam - Employment force",fontsize=12)
ax[0,0].legend(loc="lower center")

ax[0,1].bar(year,df21FU["Vietnam"],0.25,yerr=[.5,.5,.5,.5],label="Women",color="orange")
ax[0,1].bar(year,df21MU["Vietnam"],0.25,label="Men",bottom=df21FU["Vietnam"],yerr=[.5,.5,.5,.5],color="wheat")
ax[0,1].set_title("Vietnam - Unemployment force",fontsize=12)
ax[0,1].legend(loc="lower center")

ax[0,2].bar(year,df21FE["Mexico"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,2].bar(year,df21ME["Mexico"],0.25,label="Men",bottom=df21FE["Mexico"],yerr=lst2,color="pink")
ax[0,2].set_title("Mexico - Employment force",fontsize=12)
ax[0,2].legend(loc="lower center")

ax[0,3].bar(year,df21FU["Mexico"],0.25,yerr=lst1,label="Women",color="orange")
ax[0,3].bar(year,df21MU["Mexico"],0.25,label="Men",bottom=df21FU["Mexico"],yerr=lst1,color="wheat")
ax[0,3].set_title("Mexico - Unemployment force",fontsize=12)
ax[0,3].legend(loc="lower center")

ax[1,0].bar(year,df21FE["Brazil"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[1,0].bar(year,df21ME["Brazil"],0.25,label="Men",bottom=df21FE["Brazil"],yerr=lst2,color="pink")
ax[1,0].set_title("Brazil - Employment force",fontsize=12)
ax[1,0].legend(loc="lower center")

ax[1,1].bar(year,df21FU["Brazil"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,1].bar(year,df21MU["Brazil"],0.25,label="Men",bottom=df21FU["Brazil"],yerr=lst1,color="wheat")
ax[1,1].set_title("Brazil - Unemployment force",fontsize=12)
ax[1,1].legend(loc="lower center")

ax[1,2].bar(year,df21FE["Algeria"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[1,2].bar(year,df21ME["Algeria"],0.25,label="Men",bottom=df21FE["Algeria"],yerr=lst2,color="pink")
ax[1,2].set_title("Algeria - Employment force",fontsize=12)
ax[1,2].legend(loc="lower center")

ax[1,3].bar(year,df21FU["Algeria"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,3].bar(year,df21MU["Algeria"],0.25,label="Men",bottom=df21FU["Algeria"],yerr=lst1,color="wheat")
ax[1,3].set_title("Algeria - Unemployment force",fontsize=12)
ax[1,3].legend(loc="lower center")

ax[2,0].bar(year,df21FE["India"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[2,0].bar(year,df21ME["India"],0.25,label="Men",bottom=df21FE["India"],yerr=lst2,color="pink")
ax[2,0].set_title("India - Employment force",fontsize=12)
ax[2,0].legend(loc="lower center")

ax[2,1].bar(year,df21FU["India"],0.25,yerr=lst1,label="Women",color="orange")
ax[2,1].bar(year,df21MU["India"],0.25,label="Men",bottom=df21FU["India"],yerr=lst1,color="wheat")
ax[2,1].set_title("India - Unemployment force",fontsize=12)
ax[2,1].legend(loc="lower center")

ax[2,2].bar(year,df21FE["Russian Federation"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[2,2].bar(year,df21ME["Russian Federation"],0.25,label="Men",bottom=df21FE["Russian Federation"],yerr=lst2,color="pink")
ax[2,2].set_title("Russian Federation - Employment force",fontsize=12)
ax[2,2].legend(loc="lower center")

ax[2,3].bar(year,df21FU["Russian Federation"],0.25,yerr=lst1,label="Women",color="orange")
ax[2,3].bar(year,df21MU["Russian Federation"],0.25,label="Men",bottom=df21FU["Russian Federation"],yerr=lst1,color="wheat")
ax[2,3].set_title("Russian Federation - Unemployment force",fontsize=12)
ax[2,3].legend(loc="lower center")

plt.savefig("labort21.png")


# In[24]:


fig, ax = plt.subplots(2,5)
fig.set_size_inches(40,20, forward = True)
fig.suptitle("Developped countries T2.2 Labor decisions of men and women 2018-2021", fontsize = 14.5)

lst1=[1,1,1,1]
lst2=[2,2,2,2]

year=["2018","2019","2020","2021"]

ax[0,0].bar(year,df22FE["Ukraine"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,0].bar(year,df22ME["Ukraine"],0.25,label="Men",bottom=df22FE["Ukraine"],yerr=lst2,color="pink")
ax[0,0].set_title("Ukraine - Employment force",fontsize=12)
ax[0,0].legend(loc="lower center")

ax[1,0].bar(year,df22FU["Ukraine"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,0].bar(year,df22MU["Ukraine"],0.25,label="Men",bottom=df22FU["Ukraine"],yerr=lst1,color="wheat")
ax[1,0].set_title("Ukraine - Unemployment force",fontsize=12)
ax[1,0].legend(loc="lower center")

ax[0,1].bar(year,df22FE["Sri Lanka"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,1].bar(year,df22ME["Sri Lanka"],0.25,label="Men",bottom=df22FE["Sri Lanka"],yerr=lst2,color="pink")
ax[0,1].set_title("Sri Lanka - Employment force",fontsize=12)
ax[0,1].legend(loc="lower center")

ax[1,1].bar(year,df22FU["Sri Lanka"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,1].bar(year,df22MU["Sri Lanka"],0.25,label="Men",bottom=df22FU["Sri Lanka"],yerr=lst1,color="wheat")
ax[1,1].set_title("Sri Lanka - Unemployment force",fontsize=12)
ax[1,1].legend(loc="lower center")

ax[0,2].bar(year,df22FE["Venezuela"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,2].bar(year,df22ME["Venezuela"],0.25,label="Men",bottom=df22FE["Venezuela"],yerr=lst2,color="pink")
ax[0,2].set_title("Venezuela, RB - Employment force",fontsize=12)
ax[0,2].legend(loc="lower center")

ax[1,2].bar(year,df22FU["Venezuela"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,2].bar(year,df22MU["Venezuela"],0.25,label="Men",bottom=df22FU["Venezuela"],yerr=lst1,color="wheat")
ax[1,2].set_title("Venezuela, RB - Unemployment force",fontsize=12)
ax[1,2].legend(loc="lower center")

ax[0,3].bar(year,df22FE["Nigeria"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,3].bar(year,df22ME["Nigeria"],0.25,label="Men",bottom=df22FE["Nigeria"],yerr=lst2,color="pink")
ax[0,3].set_title("Nigeria - Employment force",fontsize=12)
ax[0,3].legend(loc="lower center")

ax[1,3].bar(year,df22FU["Nigeria"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,3].bar(year,df22MU["Nigeria"],0.25,label="Men",bottom=df22FU["Nigeria"],yerr=lst1,color="wheat")
ax[1,3].set_title("Nigeria - Unemployment force",fontsize=12)
ax[1,3].legend(loc="lower center")

ax[0,4].bar(year,df22FE["Colombia"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,4].bar(year,df22ME["Colombia"],0.25,label="Men",bottom=df22FE["Colombia"],yerr=lst2,color="pink")
ax[0,4].set_title("Colombia - Employment force",fontsize=12)
ax[0,4].legend(loc="lower center")

ax[1,4].bar(year,df22FU["Colombia"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,4].bar(year,df22MU["Colombia"],0.25,label="Men",bottom=df22FU["Colombia"],yerr=lst1,color="wheat")
ax[1,4].set_title("Colombia - Unemployment force",fontsize=12)
ax[1,4].legend(loc="lower center")

plt.savefig("labort22.png")


# In[257]:


type2_3


# In[30]:


fig, ax = plt.subplots(2,5)
fig.set_size_inches(40,20, forward = True)
fig.suptitle("Developped countries T2.3 Labor decisions of men and women 2018-2021", fontsize = 14.5)

lst1=[.5,.5,.5,.5]
lst2=[2,2,2,2]

year=["2018","2019","2020","2021"]

ax[0,0].bar(year,df23FE["Haiti"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,0].bar(year,df23ME["Haiti"],0.25,label="Men",bottom=df23FE["Haiti"],yerr=lst2,color="pink")
ax[0,0].set_title("Haiti - Employment force",fontsize=12)
ax[0,0].legend(loc="lower center")

ax[1,0].bar(year,df23FU["Haiti"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,0].bar(year,df23MU["Haiti"],0.25,label="Men",bottom=df23FU["Haiti"],yerr=lst1,color="wheat")
ax[1,0].set_title("Haiti - Unemployment force",fontsize=12)
ax[1,0].legend(loc="lower center")

ax[0,1].bar(year,df23FE["Madagascar"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,1].bar(year,df23ME["Madagascar"],0.25,label="Men",bottom=df23FE["Madagascar"],yerr=lst2,color="pink")
ax[0,1].set_title("Madagascar - Employment force",fontsize=12)
ax[0,1].legend(loc="lower center")

ax[1,1].bar(year,df23FU["Madagascar"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,1].bar(year,df23MU["Madagascar"],0.25,label="Men",bottom=df23FU["Madagascar"],yerr=lst1,color="wheat")
ax[1,1].set_title("Madagascar - Unemployment force",fontsize=12)
ax[1,1].legend(loc="lower center")

ax[0,2].bar(year,df23FE["Burundi"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,2].bar(year,df23ME["Burundi"],0.25,label="Men",bottom=df23FE["Burundi"],yerr=lst2,color="pink")
ax[0,2].set_title("Burundi - Employment force",fontsize=12)
ax[0,2].legend(loc="lower center")

ax[1,2].bar(year,df23FU["Burundi"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,2].bar(year,df23MU["Burundi"],0.25,label="Men",bottom=df23FU["Burundi"],yerr=lst1,color="wheat")
ax[1,2].set_title("Burundi - Unemployment force",fontsize=12)
ax[1,2].legend(loc="lower center")

ax[0,3].bar(year,df23FE["Cambodia"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,3].bar(year,df23ME["Cambodia"],0.25,label="Men",bottom=df23FE["Cambodia"],yerr=lst2,color="pink")
ax[0,3].set_title("Cambodia - Employment force",fontsize=12)
ax[0,3].legend(loc="lower center")

ax[1,3].bar(year,df23FU["Cambodia"],0.25,yerr=[.1,.1,.1,.1],label="Women",color="orange")
ax[1,3].bar(year,df23MU["Cambodia"],0.25,label="Men",bottom=df23FU["Cambodia"],yerr=[.1,.1,.1,.1],color="wheat")
ax[1,3].set_title("Cambodia - Unemployment force",fontsize=12)
ax[1,3].legend(loc="lower center")

ax[0,4].bar(year,df23FE["Yemen"],0.25,yerr=lst2,label="Women",color="skyblue")
ax[0,4].bar(year,df23ME["Yemen"],0.25,label="Men",bottom=df23FE["Yemen"],yerr=lst2,color="pink")
ax[0,4].set_title("Yemen - Employment force",fontsize=12)
ax[0,4].legend(loc="lower center")

ax[1,4].bar(year,df23FU["Yemen"],0.25,yerr=lst1,label="Women",color="orange")
ax[1,4].bar(year,df23MU["Yemen"],0.25,label="Men",bottom=df23FU["Yemen"],yerr=lst1,color="wheat")
ax[1,4].set_title("Yemen - Unemployment force",fontsize=12)
ax[1,4].legend(loc="lower center")

plt.savefig("labort23.png")


# ---
