### See PIN-based authorization for details at
### https://dev.twitter.com/docs/auth/pin-based-authorization
import os

import tweepy

consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_SECRET_KEY']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# get access token from the user and redirect to auth URL
auth_url = auth.get_authorization_url()
print('Authorization URL: ' + auth_url)

# ask user to verify the PIN generated in broswer
verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)

# authenticate and retrieve user name
auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth)
username = api.me().name
print('Ready to post to ' + username)
