import os
import tweepy

consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token_one = os.environ['ONE']
access_token_two = os.environ['TWO']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_one, access_token_two)
api = tweepy.API(auth)