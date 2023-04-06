#imports
import tweepy
import requests
from bs4 import BeautifulSoup
import re
import schedule
import time

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Define a function to retrieve the latest news from a specific hashtag
def get_latest_news():
    url = 'https://twitter.com/hashtag/Daybreak?src=hashtag_click'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tweets = soup.find_all('div', {'class': 'tweet'})
    latest_tweet = tweets[0].find('div', {'class': 'tweet-text'}).text.strip()
    return latest_tweet

#define a function that tweets the latest news from the #Daybreak hashtag:
def tweet_latest_news():
    latest_news = get_latest_news()
    api.update_status(latest_news)

#schedule it to run every morning at 8am 
schedule.every().day.at('08:00:00').do(tweet_latest_news)

while True:
    schedule.run_pending()
    time.sleep(1)

