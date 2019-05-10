from sklearn.linear_model import LogisticRegression
import pickle
from pprint import pprint

def main():
    lr = pickle.load(open('lr.model', 'rb'))
    bow = pickle.load(open('bow.model', 'rb'))
    coef = lr.coef_[0]
    vocab = [e[0] for e in sorted(bow.vocabulary_.items(), key=lambda x: x[1])]
    pair = list(zip(coef, vocab))

    pprint(sorted(pair, key=lambda x: x[0])[:10])
    pprint(sorted(pair, key=lambda x: -x[0])[:10])





if __name__ == '__main__':
    main()