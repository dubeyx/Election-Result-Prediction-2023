import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(Joe Biden) until:2023-01-01 since:2021-01-01"
tweets = []
limit = 500


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['user', 'text'])
df.to_csv('Biden.csv')