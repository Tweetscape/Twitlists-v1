"""
import os
import tweepy

consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token_one = os.environ['ONE']
access_token_two = os.environ['TWO']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_one, access_token_two)
api = tweepy.API(auth)
"""

import os, tweepy

api_key = os.environ['KEY']
api_secret = os.environ['SECRET']
access_token = os.environ['TOKEN']
access_token_secret = os.environ['TOKEN_SECRET']
app_secret_key = os.environ['APP_SECRET_KEY']


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Store tweet timelines from list members as a dictionary of "ResultSet" objects

the_lists =  {"gaming" : "blockchain-gaming", "gurus": "cryptogurus", "eth" : "ethereum", "econ" : "economics", "ai": "ai", "btc" :  "bitcoin", "space" :  "space", "systems" : "systems-thinkers", "cryptofunds" : "cryptofunds",
              "defi" : "decentralized-finance", "dao": "dao", "politicaleconomy" : "politicaleconomy", "network": "network", "psych" : "psych", "techexecs" : "techexecs", "vc" : "vc"}

# Using @shingaithornton twitter handle for testing app.
for slug in the_lists.keys():
    the_lists[slug] = api.list_timeline(screen_name='@shingaithornton', slug = the_lists[slug], owner_screen_name='@shingaithornton', include_rts = 'false', count = 100)


# Isolate json of tweepy "status" objects, add them into a list of dictionaries

gaming_tweets, gurus_tweets, eth_tweets, econ_tweets, ai_tweets, btc_tweets, space_tweets, systems_tweets, cryptofunds_tweets, dao_tweets, defi_tweets, network_tweets, politicaleconomy_tweets, psych_tweets, techexecs_tweets, vc_tweets = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
gaming_list, gurus_list, eth_list, econ_list, ai_list, btc_list, space_list, systems_list, cryptofunds_list, dao_list, defi_list, network_list, politicaleconomy_list, psych_list, techexecs_list, vc_list = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
