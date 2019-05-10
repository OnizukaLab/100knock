from p71 import stopwords
from nltk.stem import PorterStemmer
import nltk
import re
import string


class Feature:
    def __init__(self):
        self.target = ['NNP', 'NNPS', 'PRP', 'PRP$', 'SYM', 'DT', 'QT', 'CD', 'UNKNOWN', 'POS', 'WDT', 'WP',
                       'WP$', 'TO', 'IN', 'CC']
        self.sw = stopwords()
        self.stemmer = PorterStemmer()

    def get_feature(self, text):
        return self.transform([t[0] for t in nltk.pos_tag(list(filter(''.__ne__, text.split(' ')))) if t[1] not in self.target])

    def transform(self, text):
        words = [w for w in text if not self.sw.is_stopword(w)]

        return [self.stemmer.stem(w) for w in words]


if __name__ == '__main__':
    a = Feature()








