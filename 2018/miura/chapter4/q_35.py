from q_30 import *
import re

for sentence in allsentence:
    #[名詞,名詞,\n,\n,名詞,\n]みたいなリストを作って、文字列にし、複数回続く\nを1つにまとめている
    print(re.sub('\n+','\n',''.join([word['surface'] if word['pos'] == '名詞' else '\n' for word in sentence])).strip())

'''
tmp = []
for sentence in allsentence:
    for word in sentence:
        if word['pos'] == '名詞':
            tmp.append(word['surface'])
        else:
            if len(tmp) > 0:
                print(''.join(tmp))
                tmp = []
'''
