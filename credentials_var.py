import pymongo
import tweepy
import mysql.connector


# MySQL Database identifier & connection
sql_db_name = "dbmantap"
sqlDb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database=sql_db_name
)
sqlCursor = sqlDb.cursor()

# MongoDB Database identifier & connection
client = pymongo.MongoClient('localhost', 27017)
mongoDb = client.TweetSentimentAnalyzer
raw_tweets = mongoDb.tweets
raw_findAll = raw_tweets.find()
tokens = mongoDb.tokens
tokens_findAll = tokens.find()

# User credentials to access Twitter API
ACCESS_TOKEN = "94752564-BvP4ZNJawmbcBbZfl9V9fVxCMqBEw3C3XfspEZFbZ"
ACCESS_TOKEN_SECRET = "tXyHXu7vJt6k3YlnPNm5JI8gBbfqIfQzOVWhlKzH1GNMS"
CONSUMER_KEY = "VDUHKifMgzsf0z98tEeaqgBkU"
CONSUMER_SECRET = "ukVf6fqYeqUeZ10WeMjv0a35DfZw79INqgzEM8Rat9y2pxncr5"

# Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
