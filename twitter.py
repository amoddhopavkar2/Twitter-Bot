import tweepy
import time

auth = tweepy.OAuthHandler('r2xKxQXkxVSw9EuTjXr9zu9ds',
                           'qdSXAkPIYlUb0erefAujqVAmHI0cWCFgoctkg13Q7pMwCj70Td')

auth.set_access_token('875624513500663808-gXL8jG4DYDVsAE47psPkctLnLOju7c1',
                      'd0k6PwWiSIQiYXvQJFyBfS9eKy1fWTQMh6jT8eHzDCUPI')

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
