import json
import pymongo
import tweepy
import time
import string
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = pymongo.MongoClient('localhost', 27017).TwitterStreamDB

    def on_data(self, tweet):
        full_data = json.loads(tweet)
        print(full_data)
        self.db.tweets.insert_one(full_data)



    def on_error(self, status_code):
        print(status_code)
        return True

    def on_timeout(self):
        return True

CONSUMER_KEY = '02yhVAcQIyL8HqA043VmCytxy'
CONSUMER_SECRET = 'Oo9bPETrpHBZrsIxxmvWl2GIv7n7FoyNQLAG3m3FKK5CQ5QOgU'
ACCESS_TOKEN = '1079695581348413441-Ndj5edc4tio2VgiTZSLnEKNUoWV14m'
ACCESS_SECRET = 'AhfqaWJSSXC6qGdn3ygmavAia9WzIuthgwo50kGipmxuU'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
# the list of keywords for filtering tweets
keyword_list = ['Pemilu','Prabowo','Jokowi','presiden']
sapi.filter(track = keyword_list)
print ('Tweets have been successfully stored into mongoDB.')