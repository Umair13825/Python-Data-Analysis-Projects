# ## WORKING ON PYTHON DATA ANALYSIS PROJECT_1
# 
# #### (Part of Big Data Analysis)

# # The Weather Dataset
# 
# ##### The Dataset contains a time-series with per hour information about the weather conditions at some particular locations. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions. 
# 
# 

# In[2]:


import pandas as pd


# ### 1_ Import DataSet into Jupyter_Notebook

# In[8]:


data = pd.read_csv(r"C:\Users\Haier\Downloads\1. Weather Data.csv")


# In[9]:


data


# ### 2_ Analyze the DataFrame

# ##### .head()

# In[10]:


data.head()


# ##### .shape

# In[11]:


data.shape


# ##### .index

# In[12]:


data.index


# ##### .colums

# In[13]:


data.columns


# ##### .dtype

# In[14]:


data.dtypes


# ##### .unique()

# In[16]:


data['Weather'].unique()


# ##### .nunique()

# In[17]:


data.nunique()


# ##### .count

# In[18]:


data.count()


# ##### .value_counts

# In[19]:


data['Weather'].value_counts()


# ##### .info()

# In[20]:


data.info()


# ### Q1) Unique "Wind_Speed" values in dataset

# In[21]:


data.head(2)


# In[23]:


data.nunique()


# In[25]:


data['Wind Speed_km/h'].nunique()


# In[26]:


data['Wind Speed_km/h'].unique()


# ### Q2) Number of Times when the 'Weather is exactly clear'

# In[27]:


data.head(2)


# In[28]:


# value_counts()
data.Weather.value_counts()


# In[33]:


# filtering
# data.head(2)
data[data.Weather == 'Clear']


# In[35]:


# groupby 
# data.head(2)
data.groupby('Weather').get_group('Clear')


# ### Q3) Number of times when the 'Wind Speed is exactly 4Km/h'.

# In[36]:


data.head(2)


# In[37]:


data['Wind Speed_km/h'] == 4


# In[38]:


data [data['Wind Speed_km/h'] == 4]


# ### Q 4) Null values in the data

# In[40]:


data.isnull().sum()


# In[41]:


data.notnull().sum()


# ### Q 5) Rename column "Weather" of dataframe as "Weather Condition".

# In[42]:


data.head(2)


# In[43]:


data.rename(columns = {'Weather' : 'Weather Condition'}) ## Temporary Change


# In[44]:


data.head(2)


# In[46]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True) ## Change Name Permanently


# In[47]:


data.head(2)


# ### Q 6) 'Visibility'

# In[48]:


data.head(2)


# In[49]:


data.Visibility_km.mean()


# ### Q 7) Standard Deviation of 'Pressure' Column 

# In[50]:


data.Press_kPa.std()


# ### Q 8) Variance of "Relative Humidity" in Dataset

# In[51]:


data.head(2)


# In[53]:


data["Rel Hum_%"].var()


# ### Q 9) All instances when 'Snow' recorded

# In[57]:


# values counts()
# data.head(2)
data['Weather Condition'].value_counts()


# In[58]:


# filtering
data[data["Weather Condition"] == 'Snow']


# In[59]:


# str.constains
data[data["Weather Condition"].str.contains('Snow')]


# ### Q 10) All instances when 'Wind Speed is above 24' and 'Visibility' is 25.

# In[60]:


data.head(2)


# In[61]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# ### Q 11) Mean value of each column against each 'Weather Condition'

# In[62]:


data.head(2)


# In[63]:


data.groupby('Weather Condition').mean()


# ### Q 12) Max. and Min value of each column against each 'Weather Condition'

# In[64]:


data.head(2)


# In[65]:


data.groupby('Weather Condition').min()


# In[66]:


data.groupby('Weather Condition').max()


# ### Q 13) All records where weather condition is Fog

# In[67]:


data[data['Weather Condition'] == 'Fog']


# ### Q 14) All instances when 'Weather is Clear' or 'Visibility is above 40'

# In[68]:


data[(data['Weather Condition'] ==  'Clear') | (data['Visibility_km'] > 40)]


# ### Q 15) Find instances:

# #### A) 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'

# In[69]:


data.head(2)


# In[70]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] >40)]


# # The End
