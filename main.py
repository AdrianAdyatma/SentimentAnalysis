from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)

consumerKey = "02yhVAcQIyL8HqA043VmCytxy"
consumerSecret = "Oo9bPETrpHBZrsIxxmvWl2GIv7n7FoyNQLAG3m3FKK5CQ5QOgU"
accessToken = "1079695581348413441-Ndj5edc4tio2VgiTZSLnEKNUoWV14m"
accessTokenSecret = "AhfqaWJSSXC6qGdn3ygmavAia9WzIuthgwo50kGipmxuU"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword/hastag to search about : ")
noOfSearchTerm = int(input("Enter How many tweets yo analyze : "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerm)
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets :
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    print(100*"=")

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerm)
negative = percentage(negative, noOfSearchTerm)
neutral = percentage(neutral, noOfSearchTerm)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " +searchTerm+ " by analyzing " +str(noOfSearchTerm)+ " Tweets.")

if(polarity == 0) :
    print("Neutral")
elif(polarity < 0.00) :
    print("Negative")
elif(polarity > 0.00) :
    print("Posistive")

labels = ['Posistive [' +str(positive)+ ' %] ', 'Neutral [' +str(neutral)+ ' %] ', 'Negative [' +str(negative)+ ' %]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analizing '+str(noOfSearchTerm)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
