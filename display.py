#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st


# In[ ]:


st.write('# The Filthiest')
st.write('**The Filthiest** reads in Statcast data from Baseball Savant and calculates the filthiest pitches thrown each day.')
st.write("**FiFaX**, or **Filth Factor X** is the probability a pitch will be a swinging strike, called strike, or foul tip given that the pitch is not a ball and doesn't result in a foul ball.")
st.write('Predictions are given by a Random Forest model trained on all pitches thrown in 2021.')


# In[ ]:


date = '2021-9-1'
filename = date + '.csv'
df = pd.read_csv(filename, index_col = 0)
df = df.loc[df['result'] == 'Strike']


# In[19]:






pitch_type = st.selectbox('Pitch type:', ('4-Seam Fastball', 'Slider', '2-Seam Fastball/Sinker', 'Changeup', 'Curveball', 'Splitter/Knuckleball', 'Cutter'))

sort = st.selectbox('Sort by:', ('FiFaX', 'MPH', 'RPM', 'VBreak', 'HBreak'))

leader_index = st.selectbox('Select index:', (1,2,3,4,5))
pitch_dict = {'4-Seam Fastball': 'Fastball',
              'Slider': 'Slider',
              '2-Seam Fastball/Sinker': 'Sinker',
              'Changeup': 'Changeup',
              'Curveball': 'Curveball',
              'Splitter/Knuckleball': 'Splitter',
              'Cutter'}
sort_dict = {'FiFaX': 'fifax',
             'MPH': 'mph',
             'RPM': 'rpm',
             'VBreak': 'vbreak',
             'HBreak': 'hbreak'}


# In[20]:



st.write('The top 5 ' + pitch_type + 's from MLB games on ' + date + ', sorted by ' + sort)

pitch_type = pitch_dict[pitch_type]
sort = sort_dict[sort]


# In[25]:


is_ascending = False

leaderboard = df.loc[(df.pitch_type == pitch_type)].sort_values(by = sort, ascending = is_ascending).head()
leader = leaderboard.iloc[leader_index - 1]
leaderboard_show = leaderboard[['pitcher', 'batter', 'inning', 'mph', 'rpm', 'vbreak', 'hbreak', 'fifax']]
leaderboard_show.columns = ['Pitcher', 'Batter', 'Inning', 'Velo (mph)', 'RPM', 'VBreak', 'HBreak', 'FiFaX']
st.dataframe(leaderboard_show)


# In[22]:


st.write(f"{leader.pitcher}'s {pitch_type.lower()} to {leader.batter} in inning {str(leader.inning)}, {leader['count'][1]}-{leader['count'][4]} count.")
st.write('[Watch on MLB Film Room](https://www.mlb.com/video/search?q=' + leader.pitcher.replace(' ', '+') + '+' +     leader.batter.replace(' ', '+') + '+inning+' + str(leader.inning) + '+' + str(leader['count'][1]) + '+ball+' +     str(leader['count'][4]) + '+strike&qt=FREETEXT)')

