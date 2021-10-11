"""
To run this file you must have valid consumer keys and access tokens from a Twitter Developed Account. 
"""
# Twitter_Keys stores personal login credentials
from Twitter_Keys import consumer_key, consumer_secret, access_token, access_token_secret, example_key
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt


######## Unlocks API #######
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

######## Searching for Keyword #######
keyword = "Amazon"
max_tweets = 100
searched_tweets = [tweet for tweet in tweepy.Cursor(
    api.search, q=keyword).items(max_tweets)]

######## Analyzing Sentiment ########
positive = negative = neutral = 0

for tweet in searched_tweets:

    the_text = TextBlob(tweet.text)  # Natural Language Processing

    if the_text.sentiment.polarity > 0:
        positive += 1

    elif the_text.sentiment.polarity < 0:
        negative += 1

    else:
        neutral += 1


######## Prints ########

print(
    f"-----\nTotal Positive = {positive} \nTotal Negative = {negative} \nTotal Neutral = {neutral} \nKeyword: {keyword}\n-----\n")

######## Graphs ########
plt.style.use('fivethirtyeight')
plt.title(f"'{keyword}' Sentiment for {max_tweets} Tweets")
plt.bar(["positive", "negative", "neutral"], [positive, negative, neutral])
plt.show()
