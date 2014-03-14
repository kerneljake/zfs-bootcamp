import sys
import tweepy
import json

consumer_key="yourconsumerkeyhere"
consumer_secret="yourconsumersecrethere"
access_key = "youraccesskeyhere"
access_secret = "youraccessecrethere" 

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_key, access_secret)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
	jsondoc = json.loads(data) # data is a string
	# pretty print
        print json.dumps(jsondoc, ensure_ascii=True, indent=4, separators=(',', ': '))
	# single line
        #print json.dumps(jsondoc, ensure_ascii=True)


l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
setTerms = ['twitter']
streamer.filter(track = setTerms)
