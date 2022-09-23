
import re 
import json
import sys
from collections import Counter

jsoN_Data =  sys.argv[1]

lisT_of_Tweets = []                                    #### Initialising list of tweets
with open(jsoN_Data, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        dicT_Of_Tweets = json.loads(jsonObj)
        lisT_of_Tweets.append(dicT_Of_Tweets)


countermultiset = Counter()                                    ## Collection of hashtags stored as dictionary and their counts are stored as dictionary valuesKeeps

for t in lisT_of_Tweets:
    try:
        if "entities" in t:
            if 'hashtags' in t['entities']:              #conditional statement scanning for hashtags in each tweet.
                hasH_Tags=[]                             # Initializing list of Hastags
                for h in t['entities']['hashtags']:
                    hasH_Tags.append(h['text'])          #appends hash tags to list of tweets
                countermultiset.update(hasH_Tags)
    except TypeError:
        pass

toP_Ten_Hash = countermultiset.most_common(10)                 ## stop the highest occuring hast tags in an orderable manner in top_ten_hashtags


for ht in toP_Ten_Hash:
        print(ht[0],' ',ht[1])                        ## Prints out the top ten with some error which were ignored in favor of next occuring hash tag



