import tweepy
import json
import re
keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["EndlessQuotebot"]["consumer_key"]
consumer_secret = key["EndlessQuotebot"]["consumer_secret"]
access_token_key = key["EndlessQuotebot"]["access_token_key"]
access_token_secret = key["EndlessQuotebot"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

tmp = "https://twitter.com/EndlessQuotebot/status/"
beforeTweet = api.user_timeline(count=1)
#print(beforeTweet[0].id_str)
nextNum = beforeTweet[0].text
ret = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,nextNum)
ret = re.sub(r"\n"," ",ret)
quoteTweet = str(int(ret)+1) + "\n" + tmp + beforeTweet[0].id_str
api.update_status(quoteTweet)