from q_30 import *

for sentence in allsentence:
    for word in sentence:
        if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
            print(word)
