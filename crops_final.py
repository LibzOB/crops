#!/usr/bin/env python
# coding: utf-8

# In[2]:


data = ("C:\DataScience\Crop_recommendation.csv")
data = pd.read_csv(data)


# In[3]:


#1) Preparing the data
#Capitalizing and changing names
columns_list = data.columns.tolist()
columns_new_list = []

for column in columns_list:
    if column.lower() not in ["ph", "label"]:
        columns_new_list.append(column.capitalize())
    elif column.lower() == "label":
        columns_new_list.append("Crop recommendation")
    else :
        columns_new_list.append("pH")
        
data.columns = columns_new_list


# In[4]:


crops = data["Crop recommendation"].unique()


# In[5]:


crops_cap = []

for crop in crops:
    crops_cap.append(crop.capitalize())


# In[6]:


crops_caps = []
for crop in data["Crop recommendation"]:
    crops_caps.append(crop.capitalize())

data["Crop recommendation"] = crops_caps


# In[7]:


# filtering datasets
data_rainfall = data[["Crop recommendation","Rainfall"]].sort_values(by=["Rainfall"], ascending=True)
data_nitrogen = data[["Crop recommendation","Nitrogen"]].sort_values(by=["Nitrogen"], ascending=True)
data_potassium = data[["Crop recommendation","Potassium"]].sort_values(by=["Potassium"], ascending=True)
data_phosphorus = data[["Crop recommendation","Phosphorus"]].sort_values(by=["Phosphorus"], ascending=True)
data_temperature = data[["Crop recommendation","Temperature"]].sort_values(by=["Temperature"], ascending=True)
data_ph = data[["Crop recommendation","pH"]].sort_values(by=["pH"], ascending=True)
data_humidity = data[['Crop recommendation','Humidity']].sort_values(by=['Humidity'], ascending=True)


# In[9]:


#2) Graphs to visualise variation by each condition
thisplot = sns.catplot(
    data = data_rainfall,
    x = "Crop recommendation",
    y = "Rainfall",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)
ax.set_ylabel("Rainfall (mm)")


# In[10]:


thisplot = sns.catplot(
    data = data_temperature,
    x = "Crop recommendation",
    y = "Temperature",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[11]:


thisplot = sns.catplot(
    data = data_ph,
    x = "Crop recommendation",
    y = "pH",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[12]:


thisplot = sns.catplot(
    data = data_nitrogen,
    x = "Crop recommendation",
    y = "Nitrogen",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[13]:


thisplot = sns.catplot(
    data = data_humidity,
    x = "Crop recommendation",
    y = "Humidity",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[14]:


thisplot = sns.catplot(
    data = data_phosphorus,
    x = "Crop recommendation",
    y = "Phosphorus",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[15]:


thisplot = sns.catplot(
    data = data_potassium,
    x = "Crop recommendation",
    y = "Potassium",
    kind = "box")
ax = thisplot.ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=85)


# In[16]:


#3) Categorising the data


# In[17]:


#Adding columns for mean data for each crop
data["mean nitrogen"] = (data.groupby("Crop recommendation")["Nitrogen"].transform("mean"))
data["mean phosphorus"] = (data.groupby("Crop recommendation")["Phosphorus"].transform("mean"))
data["mean potassium"] = (data.groupby("Crop recommendation")["Potassium"].transform("mean"))
data["mean temperature"] = (data.groupby("Crop recommendation")["Temperature"].transform("mean"))
data["mean humidity"] = (data.groupby("Crop recommendation")["Humidity"].transform("mean"))
data["mean ph"] = (data.groupby("Crop recommendation")["pH"].transform("mean"))
data["mean rainfall"] = (data.groupby("Crop recommendation")["Rainfall"].transform("mean"))


# In[18]:


#Assigning crop categories for each condition according to above graphs and adding categories as columns
def categorize_nitrogen(Nitrogen):
    if Nitrogen < 30:
        return 1
    elif 30 <= Nitrogen < 60:
        return 2
    elif 60 <= Nitrogen < 85:
        return 3
    else:
        return 4
data["Nitrogen Category"] = data["mean nitrogen"].apply(categorize_nitrogen)


# In[19]:


def categorize_potassium(Potassium):
    if Potassium < 25:
        return 1
    elif 25 <= Potassium < 30:
        return 2
    elif 30 <= Potassium < 41:
        return 3
    elif 41 <= Potassium < 4125:
        return 4
    else:
        return 5


data["Potassium Category"] = data["mean potassium"].apply(categorize_potassium)


# In[20]:


def categorize_temperature(Temperature):
    if Temperature < 25:
        return 1
    elif 25 <= Temperature < 30:
        return 2
    else:
        return 3


data["Temperature Category"] = data["mean temperature"].apply(categorize_temperature)


# In[21]:


def categorize_humidity(Humidity):
    if Humidity < 40:
        return 1
    elif 40 <= Humidity < 70:
        return 2
    elif 70 <= Humidity < 85:
        return 3
    else:
        return 4
data["Humidity Category"] = data["mean humidity"].apply(categorize_humidity)


# In[22]:


def categorize_ph(pH):
    if pH < 7:
        return 1
    else:
        return 2
data["pH Category"] = data["mean ph"].apply(categorize_ph)


# In[23]:


def categorize_rainfall(Rainfall):
    if Rainfall < 75:
        return 1
    elif 75 <= Rainfall < 110:
        return 2
    elif 110 <= Rainfall < 180:
        return 3
    else:
        return 4
data["Rainfall Category"] = data["mean rainfall"].apply(categorize_rainfall)


# In[24]:


def categorize_phosphorus(Phosphorus):
    if Phosphorus < 40:
        return 1
    elif 40 <= Phosphorus < 60:
        return 2
    elif 60 <= Phosphorus < 100:
        return 3
    else:
        return 4
data["Phosphorus Category"] = data["mean phosphorus"].apply(categorize_phosphorus)


# In[29]:


# 4) 4)	Interface allowing conditions to be input to produce a list of recommended crops

user_categories = {}

for condition in data.columns:
    if condition == ("Nitrogen Category"):
        nitrogen_cat = input("What Nitrogen Category is your land in? ( 1 = < 30; 2 = 30 - 60; 3 = 60 - 85; 4 = > 85 ) ")
        user_categories[condition] = int(nitrogen_cat)
    elif condition == ("Potassium Category"):
        potassium_cat = input("What Potassium Category is your land in? ( 1 = < 25; 2 = 25 - 30; 3 = 30 - 41; 4 = >41 ) ")
        user_categories[condition] = int(potassium_cat)
    elif condition == ("Temperature Category"):
        temperature_cat = input("What Temperature Category is your land in? ( 1 = < 25; 2 = 25 - 30; 3 = > 30 ) ")
        user_categories[condition] = int(temperature_cat)
    elif condition == ("Humidity Category"):
        humidity_cat = input("What Humidity Category is your land in? ( 1 = < 40; 2 = 40 - 70; 3 = 70 - 85; 4 = > 85 ) ")
        user_categories[condition] = int(humidity_cat)
    elif condition == ("pH Category"):
        ph_cat = input("What pH Category is your land in? ( 1 = < 7; 2 = > 7 ) ")
        user_categories[condition] = int(ph_cat)
    elif condition == ("Rainfall Category"):
        rainfall_cat = input("What Rainfall Category is your land in? ( 1 = < 75; 2 = 75 - 110; 3 = 110 - 180; 4 = > 180 ) ")
        user_categories[condition] = int(rainfall_cat)
    elif condition == ("Phosphorus Category"):
        phosphorus_cat = input("What Phosphorus Category is your land in? ( 1 = < 40; 2 = 40 - 60; 3 = 60 - 100; 4 = > 100 )")
        user_categories[condition] = int(phosphorus_cat)

new_data = data.copy()
for condition, category in user_categories.items():
    new_data = new_data[new_data[condition] == category]


result_crops = new_data["Crop recommendation"].unique().tolist()


if result_crops == []:
    print("There are no suitable crops for your land")
else:
    print(f"Here are the recommended crops for your land: {', '.join (result_crops)}")

