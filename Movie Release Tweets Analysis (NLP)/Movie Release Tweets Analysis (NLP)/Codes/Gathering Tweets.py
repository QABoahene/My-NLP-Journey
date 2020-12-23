#Importing modules
import pandas as pd
import tweepy 
from twitter_config import consumer_key, consumer_secret, access_token, access_token_secret, file_name, google_sheet_name
from textblob import TextBlob
import json
import time
import csv
import gspread
from gspread_dataframe import (get_as_dataframe, set_with_dataframe)
from oauth2client.service_account import ServiceAccountCredentials

neg = 0
s_neg = 0
neu = 0
s_pos = 0
pos = 0

#listener for twitter stream
class listener(tweepy.StreamListener):
    def on_data(self, data):
        #print(data)
        all_data = json.loads(data)
        tweet = TextBlob(all_data['text']) 
        #print(tweet.raw)

        # determine if sentiment is slightly positive, positive, slightly negative, negative, or neutral
        if tweet.sentiment.polarity <= -0.5:
            sentiment = 'negative'
            neg += 1
        elif tweet.sentiment.polarity < 0 and tweet.sentiment.polarity >= -0.5:
            sentiment = 'slightly negative'
            s_neg += 1
        elif tweet.sentiment.polarity <= 0.5 and tweet.sentiment.polarity > 0:
            sentiment = 'slightly positive'
            s_pos += 1
        elif tweet.sentiment.polarity == 0:
            sentiment = 'neutral'
            neu += 1
        else:
            sentiment = 'positive'
            pos += 1

        #getting the scores of the sentiment 
        polarity = tweet.sentiment.polarity

        #extracting the necessary features 
        created_at = all_data['created_at']

        #Gathering any new hashtags that may come with tweets
        hashtags = ''
        for hashtag in all_data['entities']['hashtags']:
        	hasht = hashtag['text']
        	clean = '#' + str(hasht)
        	hashtags = clean

        #write festures into csv
        with open('wonder_woman_movie_tweets.csv', 'a', encoding = 'utf-8') as f:
             writer = csv.writer(f, delimiter = ',')
             writer.writerow((created_at, tweet, hashtags, sentiment, polarity))

             #convert csv into datafame in order to write to google sheets   
             df = pd.read_csv('wonder_woman_tweets.csv')
             #print(df)

        #connecting to the google sheets api 
        def _get_worksheet(
            key: str,
            worksheet_name: str,
            creds: '/Users/qab/Desktop/Personal/NLP Projects/NLP - Event tweets' = 'event-tweet-analysis.json',
            ) -> gspread.Worksheet:
            """ return a gspread Worksheet instance for given Google Sheets workbook/worksheet """
            scope = ["https://spreadsheets.google.com/feeds",
                     "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
            gc = gspread.authorize(credentials)
            wb = gc.open_by_key(key)
            sheet = wb.worksheet(worksheet_name)
            return sheet

        #write pandas dataframe into google sheets 
        def write(sheet: gspread.Worksheet, df: pd.DataFrame, **options) -> None:
            set_with_dataframe(sheet, df,
                         include_index=False,
                         resize=True,
                         **options)

        sh: gspread.Worksheet = _get_worksheet(file_name, google_sheet_name)
        write(sh, df)

sentiment_analysis = [neg, s_neg, neu, s_pos, pos]

if __name__ == "__main__":
    #authenticate API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #initialize stream 
    streamListener = listener()
    stream = tweepy.Stream(auth=api.auth, listener= streamListener, tweet_mode ='extended')

    with open("wonder_woman_movie_tweets.csv", "w", encoding='utf-8') as f:
       f.write('created_at, tweet, hashtags, sentiments, polarity\n')

    while True:
        try:
            #insert keywords for Twitter search
            stream.filter(track=['#WonderWoman','#wonderwoman', '#WONDERWOMAN', '#Wonderwoman', '#WonderWoman1984', '#wonderwoman1984', '#WONDERWOMAN1984', 
            '#Wonderwoman1984', '#WonderWoman2', '#wonderwoman2', '#WONDERWOMAN2', '#Wonderwoman2', '#WonderWomanMovie', '#wonderwomanmovie', '#WONDERWOMANMOVIE',
            '#Wonderwomanmovie', '#WonderWoman84', '#wonderwoman84', '#WONDERWOMAN84', '#Wonderwoman84']) 
        except tweepy.TweepError as e:
            time.sleep(3600)
            continue