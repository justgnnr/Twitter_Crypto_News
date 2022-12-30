#!/usr/bin/python3

import tweepy
import os
import json
import sqlite3


consumer_key = os.environ.get('API_KEY')
consumer_secret = os.environ.get('API_KEY_SECRET') 
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)


con = sqlite3.connect('../instance/crypto_tweet.sqlite')
cur = con.cursor()

#cur.execute("CREATE TABLE IF NOT EXISTS tweets(tweet_id, user_name, text, created_at, url)")


results = api.search_tweets("Bitcoin", count=10)

#data = []

for i in range(len(results)):
    tweet_id = results[i].id
    user_name = results[i].user.name
    text = results[i].text
    created_at = results[i].created_at.isoformat()
    try:
        url = results[i].entities['urls'][0]['expanded_url']
    except:
        url = ''

    data = (tweet_id, user_name, text, created_at, url)
    query = """INSERT INTO tweets(tweet_id, user_name, text, created_at, url) VALUES(?, ?, ?, ?, ?)"""

    cur.execute(query, data)

    con.commit()

#    tweet = {
#       "id": tweet_id,
#       "user": user,
#       "text": text,
#       "created_at": created_at,
#       "url": url
#    }



#    data.append(tweet)

#with open( "datafile.json" , "w" ) as write:
#    json.dump( data , write )



