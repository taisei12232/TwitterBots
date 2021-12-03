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

consumer_key = key["TLSentenceBot"]["consumer_key"]
consumer_secret = key["TLSentenceBot"]["consumer_secret"]
access_token_key = key["TLSentenceBot"]["access_token_key"]
access_token_secret = key["TLSentenceBot"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

followers_ids = api.get_followers(count=20)
for i in followers_ids:
    if(i.following == False) & (i.follow_request_sent == False):
        api.create_friendship(screen_name=i.screen_name)
        #print("follow:" + i.screen_name)

doushi = ['寝る']
jodoushi = ['ます']
setuzokushi = ['だから']
meishi = ['ウーパールーパー']
joshi = ['は']
kandoushi = ['ああ']
keiyoushi = ['大きい']
fukushi = ['遂に']
rentaishi = ['この']
keiyoudoushi = ['豪華']
shujoshi = ['ね']
tweets = api.home_timeline(count=500)
for tweet in tweets:
    tokens = a.analyze(tweet.text)
    #tokens = t.tokenize(tweet.text)
    for token in tokens:
        print(token)
        if (token.part_of_speech.split(',')[1] == "形容動詞語幹") & (token.reading[0] != '*'): keiyoudoushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "動詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] != "接尾") & (token.part_of_speech.split(',')[1] != "非自立"): doushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "助動詞") & (token.reading[0] != '*'): jodoushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "接続詞") & (token.reading[0] != '*'): setuzokushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "名詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] != "非自立"): meishi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "助詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] == "終助詞"): shujoshi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "助詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] == "格助詞"): joshi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "感動詞") & (token.reading[0] != '*'): kandoushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "形容詞") & (token.reading[0] != '*'): keiyoushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "副詞") & (token.reading[0] != '*'): fukushi.append(token.base_form)
        elif (token.part_of_speech.split(',')[0] == "連体詞") & (token.reading[0] != '*'): rentaishi.append(token.base_form)
start = True
middle1 = False
middle2 = False
end = False
hojo = False
devide = -1
sentence = ''
count = 0
while True:
    count += 1
    if start == 1:
        devide = random.randint(0,5)
        if devide == 0:
            sentence += meishi[random.randrange(0,len(meishi))]
            start = False
            middle1 = True
        elif devide == 1:
            if random.randint(0,3) == 0: sentence += kandoushi[random.randrange(0,len(kandoushi))] + '、'
        elif devide == 2: sentence += keiyoushi[random.randrange(0,len(keiyoushi))]
        elif devide == 3: sentence += setuzokushi[random.randrange(0,len(setuzokushi))]
        elif devide == 4: sentence += fukushi[random.randrange(0,len(fukushi))]
        elif devide == 5:
            sentence += rentaishi[random.randrange(0,len(rentaishi))] + meishi[random.randrange(0,len(meishi))]
            start = False
            middle1 = True
    elif middle1 == 1:
        sentence += joshi[random.randrange(0,len(joshi))]
        middle1 = False
        middle2 = True
    elif middle2 == 1:
        sentence += doushi[random.randrange(0,len(doushi))]
        middle2 = False
        end = True
    elif end == 1:
        #sentence += jodoushi[random.randrange(0,len(jodoushi))]
        if random.randint(0,1) == 0: sentence += shujoshi[random.randrange(0,len(shujoshi))]
        sentence += "。"
        if random.randint(0,1) == 0: break
        else:
            end = False
            start = True
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
#print(unescape(sentence))
api.update_status(unescape(sentence))
#print(count)