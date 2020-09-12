import tweepy
import time

auth = tweepy.OAuthHandler('***********************',
                           '**************************************')

auth.set_access_token('***************************************',
                      '*******************************')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = input("Enter a keyword: ")
tweet_limit = int(input("Enter the limit: "))

for tweet in tweepy.Cursor(api.search, search).items(tweet_limit):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
