# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:27:55 2021

@author: Aditi Devgan
"""

#negative_tweets.json: 5000 tweets with negative sentiments
#positive_tweets.json: 5000 tweets with positive sentiments
#tweets.20150430-223406.json: 20000 tweets with no sentiments
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized("positive_tweets.json")

#print(tweet_tokens[0])