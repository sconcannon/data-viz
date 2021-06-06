from json_date_time_enc import JSONDateTimeEncoder
import json
import datetime

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})
print('Time from datetime: ', datetime.datetime.now())
print('Time, transformed to object: ', now_str)

def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat

add_nobel_winners = [
{'category': 'Physics',
 'name': 'Gabriel Lippmann',
 'nationality': 'French',
 'sex': 'male',
 'year': 1908},
{'category': 'Literature',
 'name': 'Sigrid Undset',
 'nationality': 'Norwegian',
 'sex': 'female',
 'year': 1928},
{'category': 'Physics',
 'name': 'Hideki Yukawa',
 'nationality': 'Japan',
 'sex': 'male',
 'year': 1949}
]

# Twitter API test from ch5 of Data Visulization with Python and Javascript
import tweepy
import json
from mongo_utils import get_mongo_database

# The user credential variables to access Twitter API
access_token = "20711121-pENR4F1xK37htgnctAkDzLyMERU1eBIDge0zueilZ"
access_token_secret = "0W8WznRmGL8tSHbuBt46m6rg4xwq3vDIPNEnESWDQF0jP"
consumer_key = "YDh4XeWWdUu0j7PwvPhMWKoJt"
consumer_secret = "DE4HfvGBSqXYAR1GpyI2hBvkVVp0IaLpEiPokDafxrTCLxn7sk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# streamListener example
# this adds tweets to a MongoDB
# to use - start MongoDB from the command line 1st


class MyStreamListener(tweepy.StreamListener):
    """ Streams tweets and saves to a MongoDB database """

    def __init__(self, api, **kw):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.col = get_mongo_database('tweets', **kw)['tweets']

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")


    def on_data(self, tweet):
        datajson = json.loads(tweet)
        # grab the 'created_at' data from the Tweet to use for display
        created_at = datajson['created_at']
        # print out a message to the screen that we have collected a tweet
        print("Tweet collected at " + str(created_at))

        self.col.insert(datajson)

    def on_error(self, status):
        print('An Error has occured: ' + repr(status_code))
        return True # keep stream open

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
streamListener = MyStreamListener(api)
stream = tweepy.Stream(auth = api.auth, listener=streamListener)

# Start the stream with track list of keywords
stream.filter(track=['#Caturday'])

#connect to and access database to confirm tweet storage
# preq - connect to database from c:// with
# "C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe" --dbpath="c:\data_twitter\db"
from mongo_utils import get_mongo_database
# use these DB constants
DB_TWEETS = 'tweets'
COLL_TWEETS = 'tweets'

db = get_mongo_database(DB_TWEETS)
coll = db[COLL_TWEETS]

res = coll.find({})
print(res)





