#Importing modules and data
import streamlit as st
import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime as dt
from PIL import Image
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
st.set_option('deprecation.showPyplotGlobalUse', False)


#Reuse this data across runs
read_and_cache_csv = st.cache(pd.read_csv)
cache_image = st.cache(Image.open)
data = pd.read_csv('/Users/qab/Desktop/Personal/NLP Projects/Context Maturity (NLP)/Data/final_jon_bellion_data.csv')
image = Image.open('/Users/qab/Desktop/Personal/NLP Projects/Context Maturity (NLP)/Images/Jon Bellion.jpg')

st.title('CONTEXT MATURITY')
st.markdown("Exploring The Changes In The Lyrical Context Throughout An Artist's Discography")
st.image(image, caption = 'Jon Bellion', use_column_width = True)
st.header('Introduction To The Project')
st.markdown("""
Ah yes... so you like music, and you're also curious about NLP.

What if we could get closer to corectly analysing music lyrics with *Natural
Language Processing(NLP)*, you ask?
Well, that's what I'm hoping this project could do for you!
This project uses the benefits of *NLP* tasks to process music lyrics and perform
tasks like:
> sentiment analysis,

> toxicity (*hate speech detection*),

> drawing themes & emotions and

> lastly, topic modelling.

This gives us a pretty good opportunity to analyse and draw insights about the
changes of music lyrics per album throughout your favourite artist's discography!
In this project, I focus on Jon Bellion's music. He currently has five(*5*) albums on
Apple Music.

I hope it's cool enough for you!
""")

st.subheader('Check Out The Songs In All The Albums')
album_list = st.selectbox('Select album', data['album'].unique())
st.write('Oh! You chose ' + album_list + ', well here you go!')
album_songs = data.loc[data.album == album_list].reset_index()
album_songs = album_songs[['date_released', 'album', 'titles']]
st.dataframe(album_songs)

st.subheader('Number of songs per album')
st.markdown(''' If the data above didn't do it,
here are the number of songs in the albums by Jon Bellion''')
st.info('Hover your mouse over the plots to get more information')
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

st.markdown('**Insights:**')
st.markdown("""
Generally, Jon Bellion's albums contain ten(*10*) to fourteen(*14*) songs.
The Human Condition is the album with most songs whiles Glory Sound Prep and Translation
Through Speakers have the least(*10*) songs.
""")


st.header('Sentiment Analysis and Toxicity Detection')
st.markdown("Let's find out how positive or negative and the degree of toxicity of Jon Bellion's lyrics")
st.markdown('### Sentiment(Polarity) Analysis')
st.info('Hover your mouse over the plots to get more information')

# Sentiment polarity distribution - shows polarity range and number of songs in that range
polarity_spread = data['polarity'].iplot(asFigure = True,
    kind = 'hist',
    bins = 28, #A small database so I limited this to the number of rows so the spread will be even.
    xTitle = '<-------- NEGATIVE ------- Lyrics Polarity -------- POSITIVE ------->',
    linecolor = 'black',
    yTitle = 'Number of Songs',
    title = 'Sentiment Polarity Distribution')
st.plotly_chart(polarity_spread)

st.markdown('**Insights:**')
st.write("""
The polarity distribution here gives you an idea of the spread for the polarity of the songs.
As you can see, most of the songs populates the *neutral, slightly negative and slightly positive* polarities.
This means that when you randomly pick a Jon Bellion song out of these albums analysed, it's highly possible that the
song will be in the above area. Also, there is one song on both extreme ends of the polarity distribution.
We can further assess the polarity by viewing the individual songs, albums and their polarities in the plot below.
""")

fig = px.strip(data,
title = 'Polarity scores for songs in albums',
labels = {'album': 'Albums', 'y': 'Polarity Score'},
x = data.album,
y = data.polarity.round(3),
hover_name = 'titles',
color = 'album',
width = 700,
height = 500
)
st.plotly_chart(fig)

st.write('### Polarity changes within a song')
st.write("""
Looking at how large the lyrics of a song is, there's a posibility that the polarity of the songs will
change with time. This visualisation below shows the changes in polarity of songs in all his albums.

You can now see the swings in positivity and negativity in his songs when divided into 5 chunks.
""")

# A function to split lyrics into 'n' number of chunks
def split_text(text, n = 5):
    '''Takes in a string of text(lyrics) and splits into n equal parts, with a default of 10 equal parts.'''

    # Calculate length of text, the size of each chunk of text and the starting points of each chunk of text
    length = len(text)
    size = math.floor(length / n)
    start = np.arange(0, length, size)

    # Pull out equally sized pieces of text and put it into a list
    split_list = []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece]+size])
    return split_list

#Trying it out
list_pieces = []
for t in data.processed_lyrics:
    split = split_text(t)
    list_pieces.append(split)

#Checking the polarity for the pieces of lyric chunks
polarity_lyrics = []
for lp in list_pieces:
    polarity_piece = []
    for p in lp:
        polarity_piece.append(TextBlob(p).sentiment.polarity)
    polarity_lyrics.append(polarity_piece)

st.cache()
# Plotting for all songs
plt.rcParams['figure.figsize'] = [50, 40]

for index, title in enumerate(data.index):
    plt.subplot(8, 7, index+1)
    plt.plot(polarity_lyrics[index])
    plt.plot(np.arange(0, 5), np.zeros(5))
    plt.title(data['titles'][index], fontsize = 18)
    plt.ylim(ymin=-1, ymax=1)
    plt.xlim(xmin=0, xmax=4)
st.pyplot()

st.write('### Toxicity')
st.write("""
By using the detoxify python library, we can detect the degree of toxic comments in the songs.
This makes for a better insight into the negatively flagged songs in terms of polarity.
Here's a chart.
""")

fig = px.scatter(
data,
x = "polarity",
y = "toxicity",
labels = {'polarity': 'Polarity',
'toxicity': 'Toxicity',
'album': 'Albums'},
hover_name = 'titles',
title = 'Polarity and Toxicity Plot',
width=800,
height=600,
color = 'album'
)
st.plotly_chart(fig)

st.write('**Insights**')
st.markdown("""
Here, we can make further insights into the lyrics.
In the album polarity chart above, we could see that the two expreme songs on
the polarity scores were couple's retreat being the most negative song and guillotine
being the most positive song. But an interesting thing happens here as the polarity
against toxicity chart shows couple's retreat having a lower toxicity score.

When you listen or read the lyrics of the song, you can notice that the song isn't really
negative but there is a lot of 'sorry' in the lyrics. This can further expose the
bias of polarity measuring modules or libraries when dealing with literatures like poems, music lyrics, etc.

The plot shows the 'woke the fuck up' song as highly toxic which makes sense based on some parts of the lyrics.
Which also happens to be the second most negative song.

The toxicity library (detoxify) can also measure some other things. Use the chart below to check the other things
per albums.
""")

st.write('### Check out what the detoxify library offers')
st.info('Select what you want to see below')
options = st.selectbox(
'Choose the metric',
('toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_hate')
)
fig = px.strip(data,
title = options + ' scores for songs in albums',
labels = {'album': 'Albums', 'y': options},
x = data.album,
y = data[options].round(3),
hover_name = 'titles',
color = 'album',
width = 700,
height = 500
)
st.plotly_chart(fig)

st.write('## Topic Modelling')
st.write("""Lets see what topics can be found in Jon Bellion's Music""")

st.write('### Top words and bigrams')
st.write("""

""")
#Getting top words
def get_top_n_words(corpus, n = None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis = 0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]
common_words = get_top_n_words(data['processed_lyrics'], 20)

for word, freq in common_words:
    st.write(word, freq)
df1 = pd.DataFrame(common_words, columns = ['processed_lyrics' , 'count'])
