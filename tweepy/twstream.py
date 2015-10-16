from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
import time
import json

consumer_key = 'oEwKmh5Jz1aRNdJaTyVIg'
consumer_secret = 'oVF2vYryn5BWpc9vPDBGaMS25a0DY9rZ2IdshowbY'
access_token = '1494668053-aoRxgB9cTEqqGh1efkIz0Owoq8JFCXuMichsx1V'
access_token_secret = 'XYbCt0AvwR1n0DB5fp64YovTfGFUGSbGB8FBszsSfI'

class listener(StreamListener):
	def on_data(self, data):
		all_data = json.loads(data)
		
		print data.encode('utf-8')
		# tweet = all_data['text']
		# username = all_data['user']['screen_name']
		userId = all_data['user']['id']
		userprofile(userId)


		user = API.get_user(userId)
		print user.screen_name
		# for follower in followers:
		# 	print follower.screen_name.encode('utf-8')


		# print ((username.encode('utf-8'), tweet.encode('utf-8')))
	

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['car'])
	
