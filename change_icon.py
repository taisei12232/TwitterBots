import tweepy
import json
import datetime

keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["AC_TLE"]["consumer_key"]
consumer_secret = key["AC_TLE"]["consumer_secret"]
access_token_key = key["AC_TLE"]["access_token_key"]
access_token_secret = key["AC_TLE"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
imgs = ["./icon_img/ranran.png","./icon_img/kesepasa.png","./icon_img/nurarihyon.png","./icon_img/to-ru.png"]
now = datetime.datetime.now()
today = int(now.strftime('%d'))
api.update_profile_image(imgs[today%4])