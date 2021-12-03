import tweepy
import re
import json

keys = open('../KeysAndTokens.json','r')
key = json.load(keys)

consumer_key = key["jerryfish_64"]["consumer_key"]
consumer_secret = key["jerryfish_64"]["consumer_secret"]
access_token_key = key["jerryfish_64"]["access_token_key"]
access_token_secret = key["jerryfish_64"]["access_token_secret"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

l = []
c = 0
for tweets in api.user_timeline(screen_name="ebosi_64",include_rts=False,count=20):
    if tweets.favorited == True: break
    if c == 0:
        c += 1
        api.create_favorite(id=tweets.id)
    str=tweets.text
    #print(tweet.id)
    ret = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,str)
    ret = re.sub(r"@([_a-zA-Z0-9]+)", "" ,ret)
    ret = re.sub(r"\n"," ",ret)
    l.append(ret)

"""for i in l:
    print(i)
"""
print(len(l))
path_w = "./text/texts.txt"
with open(path_w, mode='a') as f:
    for row in l:
        f.write("<BOS>"+row+"<EOS>\n")
