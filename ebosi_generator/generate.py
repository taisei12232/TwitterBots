# coding:utf-8
import numpy as np
from chainer import cuda, Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
import chainer.functions as F
import chainer.links as L

import sys
import argparse
import _pickle as pickle
from LSTM import LSTM

import tweepy
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


BOS_INDEX = 0
EOS_INDEX = 1

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('--unit_size',        type=int,   default=100)
parser.add_argument('--seed',           type=int,   default=1)
parser.add_argument('--gpu',            type=int,   default=-1)


args = parser.parse_args()


xp = cuda.cupy if args.gpu >= 0  else np
xp.random.seed(args.seed)



vocab = pickle.load(open('data/vocab.bin','rb'))
train_data = pickle.load(open('data/train_data.bin', 'rb'))


rnn =  LSTM(len(vocab),args.unit_size)
model = L.Classifier(rnn)
if args.gpu >= 0:
    print('use GPU!')
    cuda.get_device(args.gpu).use()
    model.to_gpu()

serializers.load_npz('data/latest.model',model)

# vocabのキーと値を入れ替えたもの
ivocab = {}
for c, i in vocab.items():
    ivocab[i] = c


def get_index_a(_model):
    _model.predictor.reset_state()
    _sentence_index_a = []
    index = BOS_INDEX
    while index != EOS_INDEX:
        y = _model.predictor(xp.array([index], dtype=xp.int32))
        probability = F.softmax(y)
        probability.data[0] /= sum(probability.data[0])
        try:
            #確率によって、ランダムに１つ単語を選択
            #index = np.argmax(probability.data[0])
            index = xp.random.choice(range(len(probability.data[0])), p=probability.data[0])
            if index!=EOS_INDEX:
                #終了<EOS>でなかった場合
                _sentence_index_a.append(index)
        except Exception as e:
            print('probability error')
            break

    return _sentence_index_a

ebosi = ""
#print('\n-=-=-=-=-=-=-=-')
sentence_index_a = get_index_a(model)
#print(sentence_index_a)
for index in sentence_index_a:
    if index in ivocab:
        ebosi += ivocab[index].split("::")[0]
api.update_status(ebosi)
#print('\n-=-=-=-=-=-=-=-')

print('generated!')
