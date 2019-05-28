# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))
import nltk


# nltk.download("stopwords")


def is_stopwords(word: str):
    word = word.lower().strip()
    stopwords = nltk.corpus.stopwords.words("english")
    return word in stopwords


if __name__ == '__main__':
    # data = data_loader()
    print(is_stopwords("I"))
    print(is_stopwords("everybody"))
