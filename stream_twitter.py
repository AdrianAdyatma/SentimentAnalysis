import json
import tweepy

import credentials_var as cred


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = cred.db

    def on_data(self, tweet):
        full_data = json.loads(tweet)
        print(full_data)
        cred.coll.insert_one(full_data)

    def on_error(self, status_code):
        print(status_code)
        return True

    def on_timeout(self):
        return True


TweetStream = tweepy.streaming.Stream(cred.auth, CustomStreamListener(cred.api))

# The list of keywords for filtering tweets
keyword_list = ['RT']

# Start streaming tweets
TweetStream.filter(track=keyword_list)
