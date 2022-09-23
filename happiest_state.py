"""
Look at function getState() for how I resolve the state of each tweet.


The algorithm is pretty simple. I try to get the location of the tweet using multiple ways.

I then add up all the sentiments of the tweets in that state to a dictionary holding { state : total_sentiment } key value pairs.

Then I get the max-key from the dictionary as my answer.
"""
import re 
import json
import sys

AFIN = sys.argv[1]
jsoN_Data =  sys.argv[2]



########   We are reading the Json file of all tweets #######
list_Of_Tweets = []
with open(jsoN_Data, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        TweetsDict = json.loads(jsonObj)
        list_Of_Tweets.append(TweetsDict)

######## This section enable us to read the AFIN file by using Scores as dictionary
afinN_File = open(AFIN)
scores = {}                                   ##Initialising empty dictionary
for line in afinN_File:
    term, score = line.split("\t") 
    scores[term] = int(score) 
afinN_File.close()



########################################################

def sentiment_of_all_tweets(line):
    sentiment   = 0
    words = line.split()                         ## Splits every line
    for word in words:                           ## scans every word in list of words to return a total sentiment from every line
        if word.lower() in scores:
            sentiment += scores[word.lower()]
    return sentiment
###########################################################################################



state_happiness = {}

### Find and add up the sentiments of each state
def tweet_sentiment(line):
  sentiment = 0
  words = line.split()
  for word in words:
    if word.lower() in scores:
      sentiment += scores[word.lower()]
  return sentiment


#######


state_happiness = {}

### Find and add up the sentiments of each state
for tweet in list_Of_Tweets:
  if 'text' in tweet:
    state = None
    try:
      if tweet['place']['place_type'] == 'city':
        if tweet['place']['country_code'] == 'US':
          state = tweet['place']['full_name'][-2:]
          state = state.upper()
      else:
        state = None
    except TypeError:
      state = None
    if state:
      if state in state_happiness and isinstance(state_happiness[state], int):
        state_happiness[state] += sentiment_of_all_tweets(tweet['text'])
      else:
        state_happiness[state] = 0
      #######

max_key = max(state_happiness, key=state_happiness.get)
print(max_key)
