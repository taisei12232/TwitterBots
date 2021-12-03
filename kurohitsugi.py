from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import tweepy
import random
from xml.sax.saxutils import unescape
import json

a = Analyzer(token_filters=[CompoundNounFilter()])
#t = Tokenizer()
# 先ほど取得した各種キーを代入する
keys = open('./KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["TL_Aizen"]["consumer_key"]
consumer_secret = key["TL_Aizen"]["consumer_secret"]
access_token_key = key["TL_Aizen"]["access_token_key"]
access_token_secret = key["TL_Aizen"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

followers_ids = api.get_followers(count=20)
for i in followers_ids:
    if(i.following == False) & (i.follow_request_sent == False):
        api.create_friendship(screen_name=i.screen_name)
        #print("follow:" + i.screen_name)

doushi_renyou = ['滲み','湧き','上がり','瞬き','満ち']
doushi = ['出す','痺れる','妨げる']
meishi = ['混濁','紋章','狂気','器','眠り','鉄','王女','泥','人形','地','己']
keiyoudoushi = ['不遜','無力']
meishi_sahen = ['否定','爬行','自壊','結合','反発']
fukushi = ['絶えず']
meirei = ['知れ']
tweets = api.home_timeline(count=700)
for tweet in tweets:
    rt = tweet.entities["user_mentions"]
    if(rt != []):
        if(rt[0]["id"] == 1454082920713359360): continue
    elif(tweet.id == 1454082920713359360): continue
    tokens = a.analyze(tweet.text)
    #tokens = t.tokenize(tweet.text)
    for token in tokens:
        #print(token)
        if (token.part_of_speech.split(',')[1] == "形容動詞語幹") & (token.reading[0] != '*'): keiyoudoushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "動詞") & (token.reading[0] != '*') & (token.infl_form == "命令ｅ"): meirei.append(token.surface)
        elif (token.part_of_speech.split(',')[0] == "動詞") & (token.reading[0] != '*') & (token.infl_form == "連用形") & (token.part_of_speech.split(',')[1] == "自立") & (token.base_form != "する"): doushi_renyou.append(token.surface)
        elif (token.part_of_speech.split(',')[0] == "動詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] != "接尾") & (token.part_of_speech.split(',')[1] != "非自立") & (token.base_form != "する"): doushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "名詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] == "サ変接続"): meishi_sahen.append(token.surface)
        elif (token.part_of_speech.split(',')[0] == "名詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] != "非自立"): meishi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "副詞") & (token.reading[0] != '*'): fukushi.append(token.base_form)

scroll = doushi_renyou[random.randrange(0,len(doushi_renyou))] + doushi[random.randrange(0,len(doushi))] + meishi[random.randrange(0,len(meishi))] + "の" + meishi[random.randrange(0,len(meishi))] + "　" + keiyoudoushi[random.randrange(0,len(keiyoudoushi))] + "なる" + meishi[random.randrange(0,len(meishi))] + "の" + meishi[random.randrange(0,len(meishi))] + "　" + doushi_renyou[random.randrange(0,len(doushi_renyou))] + doushi_renyou[random.randrange(0,len(doushi_renyou))] +  "・" + meishi_sahen[random.randrange(0,len(meishi_sahen))] + "し・" + doushi[random.randrange(0,len(doushi))][:-1] + "・" + doushi_renyou[random.randrange(0,len(doushi_renyou))] + "　" + meishi[random.randrange(0,len(meishi))] + "を" + doushi[random.randrange(0,len(doushi))] + meishi_sahen[random.randrange(0,len(meishi_sahen))] + "する" + meishi[random.randrange(0,len(meishi))] + "の" + meishi[random.randrange(0,len(meishi))] + "　" + fukushi[random.randrange(0,len(fukushi))] + meishi_sahen[random.randrange(0,len(meishi_sahen))] + "する" + meishi[random.randrange(0,len(meishi))] + "の" + meishi[random.randrange(0,len(meishi))] + "　" + meishi_sahen[random.randrange(0,len(meishi_sahen))] + "せよ　" + meishi_sahen[random.randrange(0,len(meishi_sahen))] + "せよ　" + meishi[random.randrange(0,len(meishi))] + "に" + doushi_renyou[random.randrange(0,len(doushi_renyou))] + "　" + meishi[random.randrange(0,len(meishi))] + "の" + keiyoudoushi[random.randrange(0,len(keiyoudoushi))] + "を" + doushi_renyou[random.randrange(0,len(doushi_renyou))] + "　破道の九十・黒棺"
"""print(meishi)
print(doushi)
print(jodoushi)
print(setuzokushi)
print(joshi)
print(kandoushi)
print(keiyoushi)
print(fukushi)
print(rentaishi)
print(keiyoudoushi)"""
#print(doushi_renyou)
#print(unescape(scroll))
api.update_status(unescape(scroll))
#print(count)