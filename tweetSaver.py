import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv
import datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class DahliaStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        created_at = status.created_at
        created_japan_time = created_at + datetime.timedelta(hours=9)
        print(created_japan_time)


def login():
    API_KEY = os.environ["API_KEY"]
    API_SECRETKEY = os.environ["API_SECRETKEY"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(API_KEY, API_SECRETKEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


if __name__ == "__main__":
    api = login()
    dahliaStreamListener = DahliaStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=dahliaStreamListener)
    stream.sample(languages=['ja'])
