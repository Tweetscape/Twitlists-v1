""" 
A script to identify the most retweeted tweets from curated user lists
"""
import json
import config

"""
# Grab  data from twitter and dump to json and text files.
"""

class GetJSON(object):

    def __init__(self):
        pass


    def get_tweets(self, listname, listcollection):
        listcollection = []
        for each_list in config.the_lists.values():
            for each_json_tweet in each_list:
                if each_list == config.the_lists[listname]:
                    listcollection.append(each_json_tweet._json)

        return listcollection


    def combine_lsts(self, lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8):
        return lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8



    def make_json(self):
        return json.dumps(self.combine_lsts(self.get_tweets('gaming', config.gaming_tweets),
                          self.get_tweets('gurus', config.gurus_tweets),
                          self.get_tweets('eth', config.eth_tweets),
                          self.get_tweets('econ', config.econ_tweets),
                          self.get_tweets('ai', config.ai_tweets),
                          self.get_tweets('btc', config.btc_tweets),
                          self.get_tweets('space', config.space_tweets),
                          self.get_tweets('systems', config.systems_tweets)))


    def get_data(self):
        get_api_data = []
        all_data = json.loads(self.make_json())

        for each_dict in all_data:
            text = each_dict['text']
            retweet_count = each_dict['retweet_count']
            favorite_count = each_dict['favorite_count']
            username = each_dict['user']['name']
            created_at = each_dict['created_at']

            try:
                url = each_dict['entities']['urls'][0]['url']
            except:
                url = 'none'

            get_api_data.append({
                'twitter data': {
                    'text': str(text),
                    'retweet_count': int(retweet_count),
                    'url': str(url),
                    'combo': (int(retweet_count) + int(favorite_count)),
                    'username': str(username),
                    'created_at': str(created_at)
                }
            })

        return get_api_data