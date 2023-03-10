#!/usr/bin/python3

import tweepy
import os
import json
import sqlite3

search_terms = ["Cryptocurrencies", "Cryptocurrency", "Crypto", "crypto", "Bitcoin", "Ethereum", "Tether", "USD", "BNB", "XRP", "Binance", "Dogecoin", "Cardano", "Polygon"]


def auth():
    consumer_key = os.environ.get('API_KEY')
    consumer_secret = os.environ.get('API_KEY_SECRET') 
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

    return (api)

def search_tweets(search_term, api, cur, con):

    results = api.search_tweets(search_term, count=10)


    for i in range(len(results)):

        tweet_id = results[i].id
        topic = search_term
        user_name = results[i].user.name
        text = results[i].text
        created_at = results[i].created_at.isoformat()
        url = f"https://twitter.com/twitter/statuses/{tweet_id}"

        data = (tweet_id, topic, user_name, text, created_at, url)

        try:
            query = """INSERT INTO tweets(tweet_id, topic, user_name, text, created_at, url) VALUES(?, ?, ?, ?, ?, ?)"""
            cur.execute(query, data)
            con.commit()
        except:
            break



        print("Results added to database.")



if __name__ == "__main__":
    con = sqlite3.connect('../instance/crypto_tweet.sqlite')
    cur = con.cursor()

    api = auth()

    for i in range(0, len(search_terms)):
        search_tweets(search_terms[i], api, cur, con)

    print("Done")
