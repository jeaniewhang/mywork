import tweepy
# Keys and Access Tokens

CONSUMER_KEY    = 'otMhi9PbrOtx6SxN7hRxu6U1J'
CONSUMER_SECRET = 'oIiGNxr9H2DG89qPE5OYUdRrE7uigZrqo6KhKuffIhBHiSZxr1'

ACCESS_TOKEN    = '1017154796027969536-YLdIxq7kMgHvP72BT9pfWzIXnrBGsp'
ACCESS_SECRET   = 'Q4RyyMZMHpyfoP3y5M2qfzvXEeUOTT43F8GKgVn1NioGJ'

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
api.update_status("send help sos")
