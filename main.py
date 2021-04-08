# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:27:55 2021

@author: Aditi Devgan
"""

#negative_tweets.json: 5000 tweets with negative sentiments
#positive_tweets.json: 5000 tweets with positive sentiments
#tweets.20150430-223406.json: 20000 tweets with no sentiments
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

stop_words = stopwords.words("english")
positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized("positive_tweets.json")

#Applying lemmatizer
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence

#print(lemmatize_sentence(tweet_tokens[0]))

#Removing noise 

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens
        
#print(remove_noise(tweet_tokens[0], stop_words))

#Clean all positive and negative tweets
positive_tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweets_tokens = twitter_samples.tokenized('negative_tweets.json')    

cleaned_positive_tokens_list = []
cleaned_negative_tokens_list = []

for tokens in positive_tweets_tokens:
    cleaned_positive_tokens_list.append(remove_noise(tokens, stop_words))

for tokens in negative_tweets_tokens:
    cleaned_negative_tokens_list.append(remove_noise(tokens, stop_words))
    
print(positive_tweets_tokens[500])
print(cleaned_positive_tokens_list[500])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            


























