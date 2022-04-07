#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:



st.write('# The Filthiest')


# In[ ]:


date = '2021-9-1'
filename = date + '.csv'
df = pd.read_csv(filename, index_col = 0)
df['fifax'] = df['fifax'] * 100
pd.options.display.float_format = "{:,.2f}".format


# In[19]:


pitch_type_in = st.sidebar.selectbox('Pitch type:', ('4-Seam Fastball', 'Slider', '2-Seam Fastball/Sinker', 'Changeup', 'Curveball', 'Splitter/Knuckleball', 'Cutter'))

sort_in = st.sidebar.selectbox('Sort by:', ('FiFaX', 'MPH', 'RPM', 'VBreak', 'HBreak'))

leader_index = st.sidebar.selectbox('Select index:', (1,2,3,4,5))
pitcher_search = st.sidebar.text_input('Pitcher search:', value = '')
hitter_wins = st.sidebar.checkbox('Show hitter victories instead')


st.sidebar.write('**The Filthiest** reads in Statcast data from Baseball Savant and calculates the filthiest pitches thrown each day.')
st.sidebar.write("**FiFaX**, or **Filth Factor eXpected**, is the probability a pitch will be a swinging strike, called strike, or foul tip, given that the pitch is a strike or put in play.")
st.sidebar.write('Predictions are given by a Random Forest model trained on all pitches thrown in 2021.')
st.sidebar.write('Created by Dayv Doberne | [Twitter](https://www.twitter.com/Sunyveil_Sports)')
st.sidebar.write('Inspired by [Pitching Ninja](https://twitter.com/PitchingNinja)')


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



pitch_type = pitch_dict[pitch_type_in]
sort = sort_dict[sort_in]


# In[25]:


if hitter_wins:
    df = df.loc[(df['result_raw'] == 'In play, no out') | (df['result_raw'] == 'In play, run(s)')]
else:
    df = df.loc[df['result'] == 'Strike']

is_ascending = False

leaderboard = df.loc[(df.pitch_type == pitch_type)].sort_values(by = sort, ascending = is_ascending)
if pitcher_search != '':
    leaderboard = leaderboard.loc[leaderboard['pitcher'].apply(lambda pitcher_name: pitcher_search.lower() in pitcher_name.lower())]
if len(leaderboard) > 0:
    show_n = min(len(leaderboard), 5)
    if leader_index <= show_n:
        leader = leaderboard.iloc[leader_index - 1]
    leaderboard_show = leaderboard[['pitcher', 'batter', 'mph', 'rpm', 'vbreak', 'hbreak', 'fifax']]
    leaderboard_show.columns = ['Pitcher', 'Batter', 'Velo (mph)', 'RPM', 'VBreak', 'HBreak', 'FiFaX']
    leaderboard_show.index = range(1, len(leaderboard_show) + 1)
    st.write(f'The top {str(show_n)} {pitch_type_in}s from MLB games on {date}, sorted by {sort_in}.')
    st.dataframe(leaderboard_show.head(show_n))
    
    if leader_index <= show_n:
        st.write(f"{leader.pitcher}'s {pitch_type.lower()} to {leader.batter} in inning {str(leader.inning)}, {leader['count'][1]}-{leader['count'][4]} count.")
        st.components.v1.iframe(f"https://www.mlb.com/video/search?q={leader.pitcher.replace(' ', '+')}+            {leader.batter.replace(' ', '+')}+inning+{str(leader.inning)}+{str(leader['count'][1])}+ball+            {str(leader['count'][4])}+strike&qt=FREETEXT", height = 600)
        
        fig = plt.figure(figsize = (12,4))
        sns.set_theme('notebook')
        ax = sns.kdeplot(x = df['fifax'])
        ax.set_xlabel('FiFaX')
        ax.annotate(f"{leader.pitcher}'s {leader.pitch_type_raw}", xy = (leader[sort], 0), xytext = (leader[sort], 0.02),
                    arrowprops = dict(color = 'red', horizontalalignment = 'right'))
        ax.set(title = f'Distribution of {sort_in} for {pitch_type_in}s on {date}')
        st.pyplot(fig)
        
    else:
        st.write('Index out of range!')
else:
    st.write('Player not found!')


# In[22]:


#st.write('[Watch on MLB Film Room](https://www.mlb.com/video/search?q=' + leader.pitcher.replace(' ', '+') + '+' + \
#    leader.batter.replace(' ', '+') + '+inning+' + str(leader.inning) + '+' + str(leader['count'][1]) + '+ball+' + \
#    str(leader['count'][4]) + '+strike&qt=FREETEXT)')


# In[ ]:




