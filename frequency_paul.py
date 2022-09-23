"""
I count all the words in every tweet.
I also maintain a default dict for every word to count it's total occurances.
"""
import re 
import json
import sys

jsoN_File = sys.argv[1]

list_Of_Tweets = []                                     ##Initialising our empty list of all tweets
with open(jsoN_File, 'r', encoding='utf-8') as f:        ## opening the json file in a readable format in python
    for jsonObj in f:
        dicT_Of_Tweets = json.loads(jsonObj)                  ## adding every object in Json dictionary to our list of tweets
        list_Of_Tweets.append(dicT_Of_Tweets)

##########################################################################################################################
totaL_Words=0                                        ### Initializing  total words
frequent_terms = {}                                  ###  creates an empty dictionary of frequent_terms
for tweet in list_Of_Tweets:                         ##  Makes sure occurences of every term is accounted for Count all instances of every term
    if 'text' in tweet:
        line = tweet['text'] 
        words = re.findall(r'[a-zA-Z\-]+', line)    ### Returns all non-overlapping matches of pattern in string,and matches are returned in the order found.
        totaL_Words += len(words)                   ### adds length of words to total words and counts them
        for word in words:
            if word not in frequent_terms:
                frequent_terms[word.lower()] = 1
            else:
                frequent_terms[word.lower()]+=1

################################################################################################################################

for terms, freq in frequent_terms.items():
    print(terms + '\t' + str(freq / totaL_Words))     ##  printing frequencies
####

