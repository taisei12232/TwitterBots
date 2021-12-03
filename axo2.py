import random
import tweepy
import json

keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["Axolotlrandbot2"]["consumer_key"]
consumer_secret = key["Axolotlrandbot2"]["consumer_secret"]
access_token_key = key["Axolotlrandbot2"]["access_token_key"]
access_token_secret = key["Axolotlrandbot2"]["access_token_secret"]

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

s = "ウーパールーパースーパーカーパーカーーーーーー"
h = "ウパルパスパカパカ"
u = h[random.randint(0,8)]
for i in range(17):
    if s[i] == "ー":
        u += h[random.randint(0,8)]
    else:    
        u += s[random.randint(0,22)]
# ツイートする
api.update_status(u)