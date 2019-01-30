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
import pandas as pd
import numpy as np

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [word for word in tokens if word not in stopwords and not word.isdigit()]

CONSUMER_KEY = '02yhVAcQIyL8HqA043VmCytxy'
CONSUMER_SECRET = 'Oo9bPETrpHBZrsIxxmvWl2GIv7n7FoyNQLAG3m3FKK5CQ5QOgU'
ACCESS_TOKEN = '1079695581348413441-Ndj5edc4tio2VgiTZSLnEKNUoWV14m'
ACCESS_SECRET = 'AhfqaWJSSXC6qGdn3ygmavAia9WzIuthgwo50kGipmxuU'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

conn =pymongo.MongoClient('localhost', 27017)
print ('Connected successfully to MongoDB!')
# create a database
db_name='StreamTwitterdb'
db=conn[db_name]
colection = db.tweets
results = colection.find()
list_results=list(results)

for record in list_results:
    print (record['text'])

# tokenizer
tweet_tokenizer = TweetTokenizer()
# punctuation list
punct = list(string.punctuation)
# download 127 Englisg stop words
import nltk
nltk.download('stopwords')
# list of stop words and punctuations
stopword_list = stopwords.words('indonesian') + punct + ['rt']

tf = Counter()
all_dates = []

for element in list_results:
    message = element['text']
    tokens = process(text = message, tokenizer = tweet_tokenizer, stopwords = stopword_list)
    # update word frequency
    tf.update(tokens)

# convert the counter to a sorted list (tf_sorted is a list of 2-tuples)
tf_list_sorted = sorted(tf.items(), key = lambda pair: pair[1], reverse = True)
# print each word and its frequency
for item in tf_list_sorted:
    print (item[0], item[1])

# print the top-30 frequent words and their frequencies
y1 = [x[1] for x in tf_list_sorted[:30]]
x1 = range(1, len(y1) + 1)
fig1 = plt.figure()
plt.bar(x1, y1)
plt.xlabel("Word index")
plt.title("Term Frequencies")
plt.ylabel("Frequency")
fig1.savefig('term_distribution.jpg')

# *** tweet time series ****
ones = np.ones(len(all_dates))
idx = pd.DatetimeIndex(all_dates)
# the actual time series
original_series = pd.Series(ones, index = idx).sort_index()
# time series with step of 10 seconds
revised_series = original_series.resample('10S').sum()

# print the time series
x2 = [x*10 for x in range(len(revised_series))]
y2 = list(revised_series)
fig2 = plt.figure()
plt.bar(x2, y2)
plt.title("Time series for real-time tweets")
plt.ylabel("Number of tweets")
plt.xlabel("Time [S]")
fig2.savefig('tweet_time_series.jpg')

