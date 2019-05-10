from q_30 import *

for sentence in allsentence:
    print('\n'.join(word['surface'] for word in sentence if word['pos'] == '動詞'))

'''
for sentence in allsentence:
    for word in sentence:
        if word['pos'] == '動詞':
            print(word['surface'])
'''
