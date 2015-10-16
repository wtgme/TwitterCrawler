
import tweepy

consumer_key = 'oEwKmh5Jz1aRNdJaTyVIg'
consumer_secret = 'oVF2vYryn5BWpc9vPDBGaMS25a0DY9rZ2IdshowbY'
access_token = '1494668053-aoRxgB9cTEqqGh1efkIz0Owoq8JFCXuMichsx1V'
access_token_secret = 'XYbCt0AvwR1n0DB5fp64YovTfGFUGSbGB8FBszsSfI'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Redirect user to Twitter to authorize
# tweepy.redirect_user(auth.get_authorization_url())

# Get access token
# auth.get_access_token("verifier_value")


api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text.encode('utf-8')

user = api.get_user('wttwme')
print user.screen_name
print user.created_at
print user.followers_count
for friend in user.friends():
	print friend.screen_name

print 'Follower List'
for follower in user.followers():
	print '------'
	print follower.screen_name


# Only iterate through the first 200 statuses
for status in tweepy.Cursor(api.user_timeline).items(200):
    print status

# Only iterate through the first 3 pages
for page in tweepy.Cursor(api.user_timeline).pages(3):
    print page