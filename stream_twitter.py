import json
import tweepy

import credentials_var as cred


class CustomStreamListener(tweepy.StreamListener):
    count = 0

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = cred.mongoDb

    def on_data(self, tweet):
        full_data = json.loads(tweet)
        print(full_data)
        cred.raw_tweets.insert_one(full_data)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_timeout(self):
        return True


tweetStream = tweepy.Stream(cred.auth, CustomStreamListener(cred.api))

# The list of keywords for filtering tweets
keywordList = ['jokowi','prabowo']

# Start streaming tweets
tweetStream.filter(track=keywordList)
