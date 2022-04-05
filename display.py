#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st


# In[19]:


date = '2021-9-1'
filename = '9/' + date
pitch_type = 'Curveball'


# In[20]:


st.write('# The Filthiest')
st.write('The top 5 ' + pitch_type + 's from MLB games on ' + date)


# In[21]:


df = pd.read_csv(filename, index_col = 0)
leaderboard = df.loc[(df.pitch_type == pitch_type) & (df.result == 'Swinging Strike')].sort_values(by = 'rpm', ascending = False).head()
leader = leaderboard.iloc[0]
leaderboard_show = leaderboard[['pitcher', 'batter', 'inning', 'mph', 'rpm', 'vbreak', 'hbreak']]
leaderboard_show.columns = ['Pitcher', 'Batter', 'Inning', 'Velocity (mph)', 'RPM', 'VBreak', 'HBreak']
st.dataframe(leaderboard_show)


# In[22]:


st.write(f"{leader.pitcher}'s {pitch_type.lower()} to {leader.batter} in inning {str(leader.inning)}, {leader['count'][0]}-{leader['count'][1]} count.")
st.write('[Watch on MLB Film Room](https://www.mlb.com/video/search?q=' + leader.pitcher.replace(' ', '+') + '+' +     leader.batter.replace(' ', '+') + '+inning+' + str(leader.inning) + '+' + str(leader['count'][0]) + '+ball+' +     str(leader['count'][1]) + '+strike&qt=FREETEXT)')


# In[ ]:




