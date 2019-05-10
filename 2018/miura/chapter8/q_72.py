from q_71 import *
from nltk import stem
stemmer = stem.PorterStemmer()
from collections import Counter

counter = Counter()
with open('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt') as f:
    for line in f:
        counter += Counter([stemmer.stem(word) for word in line.strip().split() if not isstop(word)])
feature_num = 1000
feature_list = [c[0] for c in counter.most_common(feature_num)]
feature_dict = {}
for i,word in enumerate(feature_list):
    feature_dict[word] = i

def seq2feat(seq):
    feat = [0 for _ in range(feature_num)]
    word_list = [stemmer.stem(word) for word in seq.strip().split()]
    for word in word_list:
        if word in feature_dict:
            feat[feature_dict[word]] += 1
    return feat
