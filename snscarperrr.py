import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "web scraping"

limit = 2
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
   if len(tweets) == limit:
       break
   else:
       tweets.append([tweet.date, tweet.user.username, tweet.content])
