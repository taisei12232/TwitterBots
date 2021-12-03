from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *

a = Analyzer(token_filters=[CompoundNounFilter()])
tokens = a.analyze("やれ しね　往ね　勝て 負けろ　知れ よくみる　より自壊する")

for token in tokens:
    if (token.part_of_speech.split(',')[0] == "名詞") & (token.reading[0] != '*') & (token.part_of_speech.split(',')[1] == "サ変接続"): print("\n\n")
    print(token)
