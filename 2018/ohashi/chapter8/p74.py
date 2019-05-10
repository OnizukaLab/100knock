from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from p72 import Feature

class Predictor:
    def __init__(self, model_file=None, bow_file=None):
        if model_file is not None:
            self.model = pickle.load(open(model_file, 'rb'))
        else:
            self.model = LogisticRegression()
        if bow_file is not None:
            self.bow = pickle.load(open(bow_file, 'rb'))
        self.feature = Feature()

    def train(self, x, y):
        inputs = self.bow.transform([' '.join(self.feature.get_feature(t)) for t in x])
        self.model.fit(inputs, y)

    def predict(self, text):
        input_vector = self.bow.transform([' '.join(self.feature.get_feature(text))])
        return self.model.predict_proba(input_vector)[0][1]


if __name__ == '__main__':
    model = Predictor(model_file='lr.model', bow_file='bow.model')

    while True:
        text = input()
        p = model.predict(text)
        if p > 0.5:
            print('+1 {}'.format(p))
        else:
            print('-1 {}'.format(p))