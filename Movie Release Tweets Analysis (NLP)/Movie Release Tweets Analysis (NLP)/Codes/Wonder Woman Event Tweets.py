import tweepy 
from credentials import consumer_key, consumer_secret, access_key, access_secret, FILE_KEY, SHEET_NAME
from textblob import TextBlob
import json
import time
import csv
import gspread
from gspread_dataframe import (get_as_datafraame,
                               set_with_dataframe)
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd





#listener for twitter stream

class listener(tweepy.StreamListener):
    def on_data(self, data):
        #print(data)


        all_data = json.loads(data)

        tweet = TextBlob(all_data["text"]) 
        #print(tweet.raw)
        


        # determine if sentiment is positive, negative, or neutral
        #if tweet.sentiment.polarity < -0.5:
            #sentiment = "negative"
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        #elif tweet.sentiment.polarity >= -0.5 and tweet.sentiment.polarity <0:
        	#sentiment ='slightly negative'
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        #elif tweet.sentiment.polarity >0 and tweet.sentiment.polarity <= 0.5:
        	#sentiment ='slightly positive'
        else:
            sentiment = "positive"

        #getting the scores of the sentiment 
        polarity = tweet.sentiment.polarity

        #extracting the necessary features 
        name = all_data["user"]['name']
        username = all_data["user"]['screen_name']
        created_at = all_data["created_at"]


        hashtags = ''
        for hashtag in all_data["entities"]['hashtags']:
        	hasht = hashtag["text"] 
        	clean = '#' + str(hasht)
        	hashtags = clean

        #write festures into csv
        with open("Tweets.csv", "a", encoding='utf-8') as f:
             writer = csv.writer(f, delimiter=',')
             writer.writerow((name, username,tweet,created_at,hashtags, sentiment, polarity))

             #convert csv into datafame in order to write to google sheets   
             df = pd.read_csv('Tweets.csv')
             #print(df)

        #connecting to the google sheets api 
        def _get_worksheet(
            key:str,
            worksheet_name:str,
            creds:"/Users/dzidzi_quist/Desktop/project"="credential.json",
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

        sh: gspread.Worksheet = _get_worksheet(FILE_KEY, SHEET_NAME)
        write(sh, df)
        

if __name__ == "__main__":
    #authenticate 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

 #initialize stream 
    streamListener = listener()
    stream = tweepy.Stream(auth=api.auth, listener= streamListener, tweet_mode ='extended')

    with open("Tweets.csv", "w", encoding='utf-8') as f:
        #f.write("username, tweet,created_at,favorite_count,retweet_count,reply_count,sentiments\n")
       f.write("name, username, tweet,created_at,hashtags, sentiments, polarity\n")

    while True:
        try:
            #insert keywords for Twitter search
            stream.filter(track=['@ECGhanaOfficial', '@NAkufoAddo','@JDMahama','#ghanaelections2020', '#LetTheCitizenKnow', '#GhanaElections',
            '#4More4Nana', '#JohnMahama2020', '#votenumber2', '#ElectionCommandCentre','#ElectionHQ','#VoteJohnMahama', '#GhanaDecides', 
            '#VoteToRetainAkufoAddo', '#VoteNumber1', '#Number1OnTheBallot', '#iChooseJM', '#GoVoteJohnMahama']) 
        except tweepy.TweepError as e:
            time.sleep(3600)
            continue