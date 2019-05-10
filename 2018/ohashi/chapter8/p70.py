import random
sentences = []

with open('rt-polarity.neg', encoding='utf-8', errors='ignore') as f:
    [sentences.append('-1 '+str_) for str_ in f]

with open('rt-polarity.pos', encoding='utf-8', errors='ignore') as f:
    [sentences.append('+1 '+str_) for str_ in f]

random.shuffle(sentences)

with open('sentiment.txt', 'w', encoding='utf-8') as f:
    [f.write(str_) for str_ in sentences]

