#Importing modules and data
import streamlit as st
import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime as dt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 15
width = 0.75
sns.set_palette(sns.color_palette('tab20', 20))
import plotly.graph_objs as go
from datetime import date, timedelta
from empath import Empath
lexicon = Empath()
import math
from textblob import TextBlob
from detoxify import Detoxify
import chart_studio.plotly as py
from plotly.offline import iplot
import plotly.express as px
import plotly.figure_factory as ff
import cufflinks
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



#Reuse this data across runs
read_and_cache_csv = st.cache(pd.read_csv)
data = pd.read_csv('/Users/qab/Desktop/Personal/NLP Projects/Context Maturity (NLP)/Data/jon_bellion.csv')


#Finds the empath themes in the lyrics
def extract_empath(lyrics):
    return lexicon.analyze(lyrics)

#Creates tags with the empath themes based on score
def make_tags(tags):
    tgs = [k for k, v in tags.items() if v != 0] #Helps set limit on tags to be kept
    #tgs = sorted(tags.items(), key = lambda x: x[1], reverse = True)
    return tgs

#Processes the dictionary of tags and keeps the keys
def process(st):
    st = str(st)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_s = st.translate(table)
    return new_s

data['empath_themes'] = data['lyrics'].apply(extract_empath).apply(make_tags).apply(process).apply(lambda x: ''.join(x))


st.write('''
# CONTEXT MATURITY
**See how your favourite artist's music changed throughout their discographies**
''')
# albums = st.selectbox(
# 'List of songs in each album', data['album'].unique()
# )
#st.dataframe(data.loc[data.album] == albums)
#Number of songs per album

st.subheader('Number of songs per album')
st.markdown('''Here are the number of songs in the albums by Jon Bellion''')
num_songs = data.groupby('album').count()['titles'].sort_values(ascending=True)
fig = num_songs.iplot(asFigure = True,
    kind='bar',
    yTitle='Number of songs',
    linecolor='black',
    opacity=0,
    title='Bar chart of songs per album release',
    xTitle='Albums'
    )
st.plotly_chart(fig)
#
# album_list = st.selectbox('Filter to:', ['album'])
# st.write(data[data.album == album_list])
