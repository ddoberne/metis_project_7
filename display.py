#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st


# In[ ]:



st.write('# The Filthiest')
st.sidebar.write('**The Filthiest** reads in Statcast data from Baseball Savant and calculates the filthiest pitches thrown each day.')
st.sidebar.write("**FiFaX**, or **Filth Factor eXpected**, is the probability a pitch will be a swinging strike, called strike, or foul tip, given that the pitch is a strike or put in play.")
st.sidebar.write('Predictions are given by a Random Forest model trained on all pitches thrown in 2021.')
st.sidebar.write('Created by Dayv Doberne | [Twitter](https://www.twitter.com/Sunyveil_Sports)')


# In[ ]:


date = '2021-9-1'
filename = date + '.csv'
df = pd.read_csv(filename, index_col = 0)
df = df.loc[df['result'] == 'Strike']
df['mph'] = df['mph'].round(decimals = 2)
df['fifax'] = df['fifax'].round(decimals = 3)


# In[19]:






pitch_type = st.sidebar.selectbox('Pitch type:', ('4-Seam Fastball', 'Slider', '2-Seam Fastball/Sinker', 'Changeup', 'Curveball', 'Splitter/Knuckleball', 'Cutter'))

sort = st.sidebar.selectbox('Sort by:', ('FiFaX', 'MPH', 'RPM', 'VBreak', 'HBreak'))

leader_index = st.sidebar.selectbox('Select index:', (1,2,3,4,5))
pitch_dict = {'4-Seam Fastball': 'Fastball',
              'Slider': 'Slider',
              '2-Seam Fastball/Sinker': 'Sinker',
              'Changeup': 'Changeup',
              'Curveball': 'Curveball',
              'Splitter/Knuckleball': 'Splitter',
              'Cutter': 'Cutter'}
sort_dict = {'FiFaX': 'fifax',
             'MPH': 'mph',
             'RPM': 'rpm',
             'VBreak': 'vbreak',
             'HBreak': 'hbreak'}


# In[20]:


show_n = 5
st.write(f'The top {str(show_n)} {pitch_type}s from MLB games on {date}, sorted by {sort}.')

pitch_type = pitch_dict[pitch_type]
sort = sort_dict[sort]


# In[25]:


is_ascending = False

leaderboard = df.loc[(df.pitch_type == pitch_type)].sort_values(by = sort, ascending = is_ascending).head()
leader = leaderboard.iloc[leader_index - 1]
leaderboard_show = leaderboard[['pitcher', 'batter', 'inning', 'mph', 'rpm', 'vbreak', 'hbreak', 'fifax']]
leaderboard_show.columns = ['Pitcher', 'Batter', 'Inning', 'Velo (mph)', 'RPM', 'VBreak', 'HBreak', 'FiFaX']
leaderboard_show.index = range(1, show_n + 1)
st.dataframe(leaderboard_show)


# In[22]:


st.write(f"{leader.pitcher}'s {pitch_type.lower()} to {leader.batter} in inning {str(leader.inning)}, {leader['count'][1]}-{leader['count'][4]} count.")
#st.write('[Watch on MLB Film Room](https://www.mlb.com/video/search?q=' + leader.pitcher.replace(' ', '+') + '+' + \
#    leader.batter.replace(' ', '+') + '+inning+' + str(leader.inning) + '+' + str(leader['count'][1]) + '+ball+' + \
#    str(leader['count'][4]) + '+strike&qt=FREETEXT)')


# In[ ]:


st.components.v1.iframe(f"https://www.mlb.com/video/search?q={leader.pitcher.replace(' ', '+')}+    {leader.batter.replace(' ', '+')}+inning+{str(leader.inning)}+{str(leader['count'][1])}+ball+    {str(leader['count'][4])}+strike&qt=FREETEXT", height = 600)

