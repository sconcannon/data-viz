#test tweepy StreamListener
import tweepy
# The user credential variables to access Twitter API
access_token = "20711121-pENR4F1xK37htgnctAkDzLyMERU1eBIDge0zueilZ"
access_token_secret = "0W8WznRmGL8tSHbuBt46m6rg4xwq3vDIPNEnESWDQF0jP"
consumer_key = "YDh4XeWWdUu0j7PwvPhMWKoJt"
consumer_secret = "DE4HfvGBSqXYAR1GpyI2hBvkVVp0IaLpEiPokDafxrTCLxn7sk"
# connect
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 1. Create a listener class
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

# 2.  Create a stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# 3. Start a Stream (use something trending on twitter
myStream.filter(track=['Notre Dame'])