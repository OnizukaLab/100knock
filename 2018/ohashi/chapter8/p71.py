class stopwords:
    def __init__(self):
        self.stopwords = ['is', 'and', 'or', 'are', 'am']

    def is_stopword(self, word):
        return word in self.stopwords


if __name__ == '__main__':
    sw = stopwords()
    assert sw.is_stopword('is') is True
    assert sw.is_stopword('and') is True
    assert sw.is_stopword('as') is False
    assert sw.is_stopword('get') is False

    print('pass')