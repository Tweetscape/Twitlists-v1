import os
import tweepy

consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token_one = os.environ['ONE']
access_token_two = os.environ['TWO']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_one, access_token_two)
api = tweepy.API(auth)


# Store tweet timelines from list members as a dictionary of "ResultSet" objects

the_lists =  {"gaming" : "Blockchain-gaming", "gurus": "Cryptogurus", "eth" : "ETH", "econ" : "Economics", "ai": "AI", "btc" :  "Bitcoin", "space" :  "Space", "systems" : "Systems"}

# Using @shingaithornton twitter handle for testing app.
for slug in the_lists.keys():
    the_lists[slug] = api.list_timeline(screen_name='@shingaithornton', slug = the_lists[slug], owner_screen_name='@shingaithornton', include_rts = 'false', count = 5000)
    
# Isolate json of tweepy "status" objects, add them into a list of dictionaries

gaming_tweets, gurus_tweets, eth_tweets, econ_tweets, ai_tweets, btc_tweets, space_tweets, systems_tweets = [],[],[],[],[],[],[],[]
gaming_list, gurus_list, eth_list, econ_list, ai_list, btc_list, space_list, systems_list  = [],[],[],[],[],[],[],[]