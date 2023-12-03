#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')


# In[3]:


filtered_year = data[(data['year'] >= 2015) & (data['year'] <= 2018)]


# In[4]:


top_players = {}


# In[5]:


for year in range(2015, 2019):
    year_data = filtered_year[filtered_year['year'] == year]
    top_players[year] = year_data.nlargest(10, ['H', 'avg', 'HR', 'OBP'])


# In[6]:


for year, top_10 in top_players.items():
    print(f"Top 10 Players in {year}:")
    print(top_10[['batter_name', 'H', 'avg', 'HR', 'OBP']])
    print("\n")


# In[7]:


data_2018 = data[data['year'] == 2018]


# In[8]:


positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']


# In[9]:


top_players_by_position_2018 = {}


# In[10]:


for position in positions:
    position_data = data_2018[data_2018['cp'] == position]
    if not position_data.empty:
        top_player = position_data.loc[position_data['war'].idxmax()]
        top_players_by_position_2018[position] = top_player[['batter_name', 'cp', 'war']]


# In[11]:


top_players_df = pd.DataFrame.from_dict(top_players_by_position_2018, orient='index')


# In[12]:


print(top_players_df)


# In[13]:


data_all_time = data.copy()


# In[14]:


stats = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']


# In[15]:


correlations = {stat: data_all_time['salary'].corr(data_all_time[stat]) for stat in stats}


# In[16]:


max_corr_stat = max(correlations, key=correlations.get)


# In[17]:


max_corr_value = correlations[max_corr_stat]


# In[18]:


print("Correlations between salary and various statistics:")
for stat, corr_value in correlations.items():
    print(f"{stat}: {corr_value:.4f}")


# In[19]:


print(f"\nStatistic with the highest correlation with salary: {max_corr_stat} ({max_corr_value:.4f})")

