# This program is used for all the data mining purposes. 
# It uses the Tweepy api for python to retrieve tweets and store it on a local database
# Author: Priya Bhatnagar

#imports
import tweepy #twitter api for python

#this class inherits from tweepy.StreamListener and overrides the constructor and on_status method
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, max_tweets = None, data = [], *args, **kwargs):
        self.counter = 0
        self.max_tweets = max_tweets
        self.data = data

        super().__init__(*args, **kwargs)

    def on_error(self ,status):
        print(status)

    def on_status(self, status):
        self.counter += 1
        if self.counter <= self.max_tweets:
            print("-----" + str(self.counter) + "------")
            print((status.text).encode('utf-8'))
            return True
        else:
            return False

#set keys
consumer_key = "nYzjahOLtjnCZAsSeBeBkMqXg" # To get a key go to apps.twitter.com 
consumer_secret = "DBPspqxUZNF6Xuzcu3gWZCX4TDN7HhMF0DxH0Gq0tmTyKYx1m1"
access_token =  "745440108891934720-FhDf9nU294AhXYee1NZCceB94P5D0Zc"
access_token_secret = "GwI9hjt9qhPPv0qK8Q3bMMEFrBjccgpqwoHLBkFbP4EZz"

def get_tweets(keyword):
    #set configuration
    auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #stream
    #create a stream by creating an instance of the listener and passing it as a parameter
    myTweetData = []
    streamListener = MyStreamListener(max_tweets = 100,  data = myTweetData)
    stream = tweepy.Stream(auth = auth, listener = streamListener)

    #start the stream 
    stream.filter(track = [keyword], languages=["en"])


get_tweets('deep learning')
