import tweepy
import random
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
from xml.sax.saxutils import unescape
import json
a = Analyzer(token_filters=[CompoundNounFilter()])
# 先ほど取得した各種キーを代入する
keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["TLOOObot"]["consumer_key"]
consumer_secret = key["TLOOObot"]["consumer_secret"]
access_token_key = key["TLOOObot"]["access_token_key"]
access_token_secret = key["TLOOObot"]["access_token_secret"]
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

followers_ids = api.get_followers(count=20)
for i in followers_ids:
    if(i.following == False) & (i.follow_request_sent == False):
        api.create_friendship(screen_name=i.screen_name)
        #print("follow:" + i.screen_name)

random_tweets = api.home_timeline(count=300)
#print(len(random_tweets))
c = 0
tweet_nouns = []
#1ツイートずつループ
while c <= 50:
    random_tweet = random_tweets[random.randint(0,len(random_tweets)-1)].text
    tokens = a.analyze(random_tweet)
    #print(random_tweet)
    for token in tokens:
        if (token.part_of_speech.split(',')[0] == "名詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] != "非自立") & (token.part_of_speech.split(',')[1] != "代名詞"):
            '''print(token.surface)
            print(token.reading)
            print(token.phonetic)
            print(token.part_of_speech)'''
            tweet_nouns.append(token)
            c += 1

"""for i in tweet_nouns:
    print(i.surface + " " +  i.part_of_speech.split(',')[1])"""
a = tweet_nouns[random.randint(0,49)]
b = tweet_nouns[random.randint(0,49)]
c = tweet_nouns[random.randint(0,49)]
#print(a.surface + "！" + b.surface + "！" + c.surface + "！" + "\n" + a.reading[0] + "・" + b.reading[0] + "・" + c.reading[0] + "、" + a.reading[0] + b.reading[0] + c.reading[0] + "、" + a.reading[0] + "・" + b.reading[0] + "・" + c.reading[0] + "！")
api.update_status(unescape(a.surface) + "!" + unescape(b.surface) + "!" + unescape(c.surface) + "!" + "\n" + a.reading[0] + "・" + b.reading[0] + "・" + c.reading[0] + "、" + a.reading[0] + b.reading[0] + c.reading[0] + "、" + a.reading[0] + "・" + b.reading[0] + "・" + c.reading[0] + "!")