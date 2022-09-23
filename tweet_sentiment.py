import json
import sys

AFIN = sys.argv[1]                             ## has afinn-111.txt. argv[1] checks for 2nd command line argument
JSON = sys.argv[2]                            ## has afinn-111.txt. argv[2] checks for 2nd command line argument

afinn = open(AFIN)                              ##opens the afinn-111.text file
scores = {}                                            # initializes an empty dictionary
for line in afinn:                                 ## for loop to assign score to the key
    term, score = line.split("\t")                      # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)                           # Convert  the score to an integer.
# print(scores.items()) # Print every (term, score) pair in the dictionary

live_tweets= []                                           ## creates an empty dictionary
# print("Started Reading JSON file which contains multiple JSON document")
with open(JSON) as f:
    for jsonObj in f:
        tweets_dict = json.loads(jsonObj)                 ### Describes how we get tweets
        live_tweets.append(tweets_dict)
# print(live_tweets[0]['text'])     ##Print first tweet only. The tweet section corresponding to the text

# line = live_tweets[0]['text']  ##
# sentimentalscore = 0  ### initialize sentimentalscore
# words = line.split()    ## Split lines in words
# for word in words :      ## going through every word in words
#              if word.lower() in scores: ## Checking if there is a csore for the word, .lower makes sure all words are lower case
#                           sentimentalscore += scores[word.lower()] ## add them to the sentimental scores if that is the case
# print(sentimentalscore)

########     Now we want to do it for all tweets(by making a function)             ######


def getscorefortweet(tweet):                           ### takes a tweet and returns a sentimental score
    line = tweet['text']                               ## assigns the text from each tweet to line
    sentimentalscore = 0                               ### initialize sentimentalscore
    words = line.split()                                ## Split lines in words
    for word in words:                                  ## going through every word in list o words
        if word.lower() in scores:                      ## condition for  tring in which all case-based characters have been lowercased.
            sentimentalscore += scores[word.lower()]
    return sentimentalscore

for tweets in live_tweets:            ### score of every tweet and adds it
    print(getscorefortweet(tweets))



