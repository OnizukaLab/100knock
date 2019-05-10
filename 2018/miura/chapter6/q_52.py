from q_51 import *
from nltk import stem

if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    for sentence in sentences_word:
        for word in sentence:
            print(word + '\t' + stemmer.stem(word))
