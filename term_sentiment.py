"""
 Take all the sentimental terms the non-sentimental term appears in tweets with, add their sentimental scores, and divide by the number of the sentimental terms.
"""


import re 
import json
import sys

AFINN = sys.argv[1]
jsoN_File =  sys.argv[2]


########################### Setting up our Dictionary of terms and their corresponding Scores  ################
scores = {}                                   #### intialising our dictionary
with open(AFINN, 'r') as afinnfile:           #### in the first part were are readding AFINN into a dictionary named scores
    for line in afinnfile:
        term, score = line.split("\t")        ### Now we are splitting each line at after the tab between term and a corresponding scorearator on the line
        scores[term] = int(score)             ### Convert  the score to an integer.



#### #####################  We are now reading the JSON file for all tweets ############################################
lisT_Of_Tweets = []                                     ## Creating an empty list of tweets
with open(jsoN_File, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        dicT_of_Tweets = json.loads(jsonObj)             ## Deserializes object in JSON file to a readable python object using a tables.append(dicT_of_Tweets)
        lisT_Of_Tweets.append(dicT_of_Tweets)

######

########################  Now we keep track of the non-sentimental terms by having them as keys made up of an emplty list  ###########################

noN_SenT_Words = {}
for tweet in lisT_Of_Tweets:                             ### For loop checking for tweet present in list of tweets
    if 'text' in tweet:                                  ### conditional statement  for words present in tweets with a corresponding sentimantal score
        line = tweet['text'] 
        words = line.split()
        for word in words:
            if word.lower() not in scores:               ## Conditional statement making sure nonsentimental words are created in an empty list
                noN_SenT_Words[word.lower()] = []


#########   Here we work on inferring the score for non-sentimental words using the ones we know from sentimental wordsall the score every non-sentimental word lets count all the scores of the sentimental words it appears with

for tweet in lisT_Of_Tweets:
    if 'text' in tweet:
        sentiments=[]                  ## Creating an emplty list for sentimental words
        line = tweet['text']
        words = line.split()

        for word in words:
            if word.lower() in scores:                           ##ensures words are in lower case and checks whether they have a score
                sentiments.append(scores[word.lower()])          ##Grabs the scores of the total sentimental words in our list of tweets
        words = line.split()
        for word in words:
            if word.lower() not in scores:
                noN_SenT_Words[word.lower()].extend(sentiments)   #puts them in the lists of all the nonsentimental words in the same tweet


############ improvised method to determine sentimental scores for all non sentimental words #####################

inferreD_Scores={}                                          ### Initializes the scores
for word in iter(noN_SenT_Words.items()):                   ### creates an object which can be iterated one element at a time
    Surrounding_scores = word[1]                           ### assigns first item in word to
    if len(Surrounding_scores)==0:
        inferreD_Scores[word[0]] = 0
        continue
    inferreD_Scores[word[0]] = sum(Surrounding_scores) / len(Surrounding_scores)   ### Calculating inferred scores using an average of scores of sentimental words by adding sentimental scores, and dividing by the number of the sentimental terms


# with open('term_sentiment_output.txt', 'w', encoding='utf-8') as f:
for word in iter(inferreD_Scores.items()):
    try:
        print(word[0]+'\t'+str(word[1]))
    except UnicodeEncodeError:
        pass


