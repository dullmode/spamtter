import os
import time
import threading

import tweepy
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

AK=os.environ.get("API_KEY")
AS=os.environ.get("API_KEY_SECRET")
AT=os.environ.get("ACCESS_TOKEN")
ATS=os.environ.get("ACCESS_TOKEN_SECRET")

QUERY=os.environ.get("QUERY")
COUNT=os.environ.get("COUNT")
INTERVAL=os.environ.get("INTERVAL")
COUNT=int(COUNT)
INTERVAL=int(INTERVAL)

auth = tweepy.OAuthHandler(AK, AS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)


def search_and_favorite(q:str, c:int):
    """
    search tweets from query and favorite all tweets.

    parameters
    ----------
    q (query)
        the word you want to search.
    c (count)
        number of tweets you serch.
        count should < 450 per 15-min, and < 1000 per day.
    """
    error_count = 0
    tweets = api.search(q=q,count=c)
    for tweet in tweets:
      tweet_id = tweet.id
      try:
          api.create_favorite(tweet_id)
      except:
          error_count += 1
          next
      time.sleep(0.3)

    print(f"number of tweets:{c}")
    print(f"number of failed:{error_count}")

def schedule(interval, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=search_and_favorite(q=QUERY, c=COUNT))
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

schedule(INTERVAL)
