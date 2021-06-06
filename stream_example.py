#test tweepy StreamListener
import tweepy
# The user credential variables to access Twitter API

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