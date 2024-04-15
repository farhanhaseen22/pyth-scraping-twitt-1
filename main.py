import pandas as pd
from ntscraper import Nitter

scraper = Nitter()
data = scraper.get_tweets("JohnCena", mode='user', number=2)

attributes_container = []

for tweet in data["tweets"]:

    attributes = {}

    attributes["link"]          = tweet["link"]
    attributes["text"]          = tweet["text"]
    attributes["name"]          = tweet["user"]["name"]
    attributes["username"]      = tweet["user"]["username"]
    attributes["date"]          = tweet["date"]
    attributes["comments"]      = tweet["stats"]["comments"]
    attributes["retweets"]      = tweet["stats"]["retweets"]
    attributes["quotes"]        = tweet["stats"]["quotes"]
    attributes["likes"]         = tweet["stats"]["likes"]

    attributes_container.append(attributes)

print(attributes_container)


df = pd.DataFrame(attributes_container)
df.to_json('scraped-tweets.json', orient='records')
# df.to_csv('scraped-tweets.csv', index=False, encoding='utf-8')



# test_list = [{'gfg': 1, 'is': 2, 'good': 3},
#              {'gfg': 2},
#              {'is': 3, 'gfg': 4}]

# print("The original list is : " + str(test_list))

# res = [d.get('is', None) for d in test_list]

# print("The values corresponding to key : " + str(res))
