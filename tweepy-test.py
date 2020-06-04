import tweepy
import json

twitter_credentials ={}
with open("clown-api-keys.json") as json_file:
    twitter_credentials = json.load(json_file)
# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_credentials["api-key"],
    twitter_credentials["api-key-secret"])
auth.set_access_token(twitter_credentials["access-token"],
    twitter_credentials["access-token-secret"])

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
