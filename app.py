# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:27:55 2021

@author: Aditi Devgan
"""

#negative_tweets.json: 5000 tweets with negative sentiments
#positive_tweets.json: 5000 tweets with positive sentiments
#tweets.20150430-223406.json: 20000 tweets with no sentiments
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
from nltk import FreqDist
import random
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from words import positive_words
from words import negative_words

stop_words = ["#","i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself","an", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","are","I","You","YouAre","You Are","you are","youare"]


positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized("positive_tweets.json")



li = list(positive_words.split(" "))
li1 = list(negative_words.split(" "))


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
        


#Clean all positive and negative tweets
positive_tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweets_tokens = twitter_samples.tokenized('negative_tweets.json')    

cleaned_positive_tokens_list = []
cleaned_negative_tokens_list = []

for tokens in positive_tweets_tokens:
    cleaned_positive_tokens_list.append(remove_noise(tokens, stop_words))
    cleaned_positive_tokens_list.append(li)

for tokens in negative_tweets_tokens:
    cleaned_negative_tokens_list.append(remove_noise(tokens, stop_words))
    cleaned_negative_tokens_list.append(li1)
    

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

all_pos_words = get_all_words(cleaned_positive_tokens_list)

freq_dist_pos = FreqDist(all_pos_words)


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

positive_tokens_for_model = get_tweets_for_model(cleaned_positive_tokens_list)
negative_tokens_for_model = get_tweets_for_model(cleaned_negative_tokens_list)

positive_dataset = [(tweet_dict, "Positive")
                     for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                     for tweet_dict in negative_tokens_for_model]

dataset = positive_dataset + negative_dataset
random.shuffle(dataset)

train_data = dataset[:15000]
test_data = dataset[15000:]      

classifier = NaiveBayesClassifier.train(train_data)

print("Accuracy is:", classify.accuracy(classifier, test_data))


#############################################################################################
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/sentiment', methods = ['GET','POST'])
def sentiment(): 
    hashtag = request.form.get('hashtag')
    custom_tokens = remove_noise(word_tokenize(hashtag))
    major = classifier.classify(dict([token, True] for token in custom_tokens))
    print(major)
    if major == "Positive":
        return render_template('sentiment.html')
    else:
        return render_template('sentimentsTemp.html')
    


if __name__ == "__main__":
    app.run(host="127.0.0.1")








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            


























