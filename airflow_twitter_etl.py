import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs


access_key = 
access_secret = 
consumer_key =
consumer_secret = 


 # Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)   
auth.set_access_token(consumer_key, consumer_secret) 

# Creating API object 
api = tweepy.API(auth)

# # # Creating an API object 
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk', 
                        # 50 is the maximum allowed count
                        count=50,
                        include_rts = False, #retweets by Elon
                        # Necessary to keep full_text 
                        # otherwise only the first 140 words are extracted
                        tweet_mode = 'extended'
                        )
#print(tweets)


tweet_list = []
for tweet in tweets:
    text = tweet._dson["ful_text"]

    refined_tweet = {"user": tweet.user.screen_name,
                     'text' : text,
                     'favorite_count' : tweet.fovorite_count,
                     'retweet_count' : tweet.retweet_count,
                     'created_at' : tweet.created_at}
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv('elonmusk_twitter_data.csv')

















