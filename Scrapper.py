import tweepy
import json
import pprint

def Scrapper():

#########################  Keys gotten from creatting my Twitter accoount   ##############################

    CONSUMER_KEY="aTlF78zGcKuaG9siNHJ4k76u3"
    CONSUMER_SECRET="Hs7zNujuKyqYqAo8o32FaaF2FXvNluxI8g1wU2ZsqggjpVWFjn"
    ACCESS_TOKEN="1301470387063095296-3ZTZsrJD7IseArp9g22CXSrf8S6P5v"
    ACCESS_SECRET="0ayRwzvIwUKJ0aNM0sGpoDSGOGGMHxUyvpUQfHVLpOuWL"

######  Authentification step created using the OAuthahndler instance into which we pass our consumer token and Access secret #############
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

####### Authentification step ##########

    user_tweets = api.home_timeline(count=5000)                   ### limiting the number of tweets to return after the count has been applied
    with open("tweets4.json", "w", encoding="utf-8") as f:       #### using the  write() method which requires a string or in this case a unicode object instead of a list. utf-8 helps encode objects which do not belong to the english alphabet
        for tweet in user_tweets:
            json.dump(tweet._json, f)                           ### dumps extracted tweets one line after another in json
            f.write('\n')                                       ### writes a file with the output separated with a new line.


if __name__ == "__main__":
    Scrapper()