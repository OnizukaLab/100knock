# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))
from collections import defaultdict
import pickle

import numpy as np
from nltk.stem import snowball
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer

from q71 import is_stopwords
from data_loader import data_loader

Y_DATAPATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/y.pkl"
X_DATAPATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/X.pkl"
VECTORIZER_DATAPATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/vectorizer.pkl"


def generate_vectors():
    y = list()
    X_data = list()
    word_dict = defaultdict(lambda: 0)
    stemer = snowball.EnglishStemmer()
    tokenizer = RegexpTokenizer(r'\w+')
    sentence_list = list()
    for sentence in data_loader():
        # ラベルと文章を切り分ける
        sentence = sentence.split()
        y.append(sentence[0])
        sentence = " ".join(sentence[1:])

        sentence = tokenizer.tokenize(sentence)
        sentence = [stemer.stem(word) for word in sentence if not is_stopwords(word)]
        for word in sentence:
            word_dict[word] += 1
        sentence_list.append(" ".join(sentence))

    # word_counts = word_dict.values()
    # import matplotlib.pyplot as plt
    # plt.hist(word_counts, bins=10, range=(0, 20))
    # plt.title("word_count histogram (all words: %d)" % len(word_dict))
    # plt.savefig("word_hist.png")
    medium_frequency_words = [key for key in word_dict.keys() if 2 < word_dict[key] < 20]
    vectorizer = CountVectorizer()
    vectorizer.fit(medium_frequency_words)

    save_vectorizer(vectorizer)

    X_data = vectorizer.transform(sentence_list)
    X_data.toarray()
    y = np.array([int(i) for i in y])
    return y, X_data


def save_data():
    y, X = generate_vectors()
    with open(Y_DATAPATH, "wb") as f:
        pickle.dump(y, f)
    with open(X_DATAPATH, "wb") as f:
        pickle.dump(X, f)


def load_data() -> (np.ndarray, np.ndarray):
    with open(Y_DATAPATH, "rb") as f:
        y = pickle.load(f)
    with open(X_DATAPATH, "rb") as f:
        X_data = pickle.load(f)
    return y, X_data


def save_vectorizer(vectorizer):
    with open(VECTORIZER_DATAPATH, "wb") as f:
        pickle.dump(vectorizer, f)


def load_vectorizer():
    with open(VECTORIZER_DATAPATH, "rb") as f:
        return pickle.load(f)


if __name__ == '__main__':
    save_data()
    y, X_data = load_data()
