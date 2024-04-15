import pandas as pd
from ntscraper import Nitter

attributes_container = []
scraper = Nitter()

data = scraper.get_tweets("TheRock", mode='user', number=2)

for tweet in data['tweets']:

    attributes = {}
    attributes["link"] = tweet["link"]
    attributes["text"] = tweet.text
    attributes["name"] = tweet.user.name
    attributes["name"] = tweet.user.username
    attributes["date"] = tweet.date
    attributes["comments"] = tweet.stats.comments
    attributes["retweets"] = tweet.stats.retweets
    attributes["quotes"] = tweet.stats.quotes
    attributes["likes"] = tweet.stats.likes
  
    attributes_container.append(attributes)

print(attributes_container)


# df.to_csv('scraped-tweets.csv', index=False, encoding='utf-8')
# df.to_json('scraped-tweets.json', orient='records', lines=True)


# test_list = [{'gfg': 1, 'is': 2, 'good': 3},
#              {'gfg': 2},
#              {'is': 3, 'gfg': 4}]

# # printing original list
# print("The original list is : " + str(test_list))

# # Using list comprehension and .get() method
# # Get values of particular key in list of dictionaries
# res = [d.get('is', None) for d in test_list]

# # printing result
# print("The values corresponding to key : " + str(res))

