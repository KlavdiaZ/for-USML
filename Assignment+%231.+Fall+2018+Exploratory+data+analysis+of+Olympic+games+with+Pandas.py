
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv("athlete_events.csv")
df.info()


# In[8]:


df.head()


# # 1. How old were the youngest male and female participants of the 1996 Olympics?

# In[9]:


df[(df["Year"]==1996) & (df["Sex"]=="F")]["Age"].min()


# In[10]:


df[(df["Year"]==1996) & (df["Sex"]=="M")]["Age"].min()


# In[11]:


df["Sport"].unique()


# # 2. What was the percentage of male gymnasts among all the male participants of the 2000 Olympics? 
# #Round the answer to the first decimal.
# #Hint: here and further if needed drop duplicated sportsmen to count only unique ones.

# In[12]:


df.drop_duplicates()
print(round((df[(df["Sex"]=="M") & (df["Year"]==2000) & (df["Sport"]=="Gymnastics")]["Sex"].value_counts() / df[(df["Sex"]=="M") & (df["Year"]==2000)]["Sex"].value_counts())*100,1))


# # 3. What are the mean and standard deviation of height for female basketball players participated in the 2000 Olympics? 
# #Round the answer to the first decimal.

# In[13]:


round(df[(df["Sex"]=="F") & (df["Year"]==2000) & (df["Sport"]=="Basketball")]["Height"].mean(),1)


# In[14]:


round(df[(df["Sex"]=="F") & (df["Year"]==2000) & (df["Sport"]=="Basketball")]["Height"].std(),1)


# # 4. Find a sportsperson participated in the 2002 Olympics, with the highest weight among other participants of the same Olympics. 
# #What sport did he or she do?

# In[15]:


df[df["Year"]==2002]["Weight"].max()


# In[16]:


df[df["Year"]==2002].sort_values(by=["Weight"],ascending=False).head()


# # 5. How many times did Pawe Abratkiewicz participate in the Olympics held in different years?

# In[17]:


df[df["Name"]=="Pawe Abratkiewicz"]["Year"].unique()


# # 6. How many silver medals in tennis did Australia win at the 2000 Olympics?

# In[18]:


df["Medal"].unique()


# In[19]:


df[(df["Sport"]=="Tennis") & (df["Medal"]=="Silver") & (df["Team"]=="Australia") & (df["Year"]==2000)]["Medal"].value_counts()


# # 7. Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics? Do not consider NaN values in Medal column.

# In[20]:


df[(df["Team"]=="Switzerland") & (df["Year"]==2016)]["Medal"].value_counts()


# In[21]:


df[(df["Team"]=="Serbia") & (df["Year"]==2016)]["Medal"].value_counts()


# # 8. What age category did the fewest and the most participants of the 2014 Olympics belong to?

# In[22]:


#[45-55] and [25-35) correspondingly
#[45-55] and [15-25) correspondingly
#[35-45] and [25-35) correspondingly
#[45-55] and [35-45) correspondingly


# In[76]:


#[15-25)
df_15=df[(df["Year"]==2014) & (df["Age"]< 25) & (df["Age"]>= 15)]["Age"].astype(int).value_counts().sum()
print(df_15)


# In[77]:


#[25-35)
df_25=df[(df["Year"]==2014) & (df["Age"]< 35) & (df["Age"]>= 25)]["Age"].astype(int).value_counts().sum()
print(df_25)


# In[78]:


#[35-45]
df_35=df[(df["Year"]==2014) & (df["Age"]<= 45) & (df["Age"]>= 35)]["Age"].astype(int).value_counts().sum()
print(df_35)


# In[79]:


#[45-55]
df_45=df[(df["Year"]==2014) & (df["Age"]<= 55) & (df["Age"]>= 45)]["Age"].astype(int).value_counts().sum()
print(df_45)


# In[81]:


print(df_45+df_25)
print(df_45+df_15)
print(df_35+df_25)
print(df_45+df_35)


# # 9. Is it true that there were Summer Olympics held in Lake Placid? Is it true that there were Winter Olympics held in Sankt Moritz?

# In[25]:


df[df["City"]=="Lake Placid"]["Season"].value_counts()


# In[26]:


df[df["City"]=="Sankt Moritz"]["Season"].value_counts()


# # 10. What is the absolute difference between the number of unique sports at the 1995 Olympics and 2016 Olympics?

# In[27]:


df1=df[df["Year"]==1995]["Sport"].unique()
print(df1)


# In[28]:


df2=df[df["Year"]==2016]["Sport"].unique()
print(df2)


# In[29]:


df3 = [x for x in df2 if x not in df1]
print(len(df3))


# In[30]:


pd.crosstab(df["Year"], df["Sport"])


# In[32]:


import numpy as np
print(np.setdiff1d(df2, df1).shape)

