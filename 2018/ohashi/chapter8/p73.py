from p72 import Feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def main():
    feature = Feature()
    with open('sentiment.txt') as f:
        data = [line.replace('\n', '').split(' ', 1) for line in f]

    inputs = [feature.get_feature(d[1]) for d in data]
    labels = [1 if d[0] == '+1' else 0 for d in data]
    bow = CountVectorizer()
    inputs = bow.fit_transform([' '.join(e) for e in inputs])

    model = LogisticRegression()
    model.fit(inputs, labels)

    print(model.score(inputs[-100:], labels[-100:]))
    pickle.dump(model, open('lr.model', 'wb'))
    pickle.dump(bow, open('bow.model', 'wb'))

if __name__ == '__main__':
    main()
