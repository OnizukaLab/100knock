from q_30 import *

for sentence in allsentence:
    print('\n'.join(word['base'] for word in sentence if word['pos'] == '動詞'))
