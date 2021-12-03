import random
import tweepy
import json

keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["Axolotl_randbot"]["consumer_key"]
consumer_secret = key["Axolotl_randbot"]["consumer_secret"]
access_token_key = key["Axolotl_randbot"]["access_token_key"]
access_token_secret = key["Axolotl_randbot"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
# Twitterオブジェクトの生成
s = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポウパルパスパカパカウパルパスパカパカ"
#s = "ウパルパスパカパカ"
u = ""
for i in range(9):
    u += s[random.randint(0,len(s))] + "ー"
# ツイートする
api.update_status(u)