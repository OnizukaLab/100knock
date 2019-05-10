from sklearn.model_selection import KFold
import pandas as pd
from p74 import Predictor
from p76 import read_data
from p77 import calc_score

def main():
    text, label = read_data('sentiment.txt')
    label = [1 if x == '+1' else 0 for x in label]

    results = []
    for train, test in KFold(n_splits=5).split(text, label):
        train_x = [text[i] for i in train]
        train_y = [label[i] for i in train]
        test_x = [text[i] for i in test]
        test_y = [label[i] for i in test]

        model = Predictor(bow_file='bow.model')
        model.train(train_x, train_y)

        preds = [model.predict(y) for y in test_x]
        results.extend([(l, int(p >= 0.5), p) for l, p in zip(label, preds)])

    true = [t[0] for t in results]
    preds = [t[1] for t in results]
    prec, recall, f1 = calc_score(true, preds)
    print('Precision = {}'.format(prec))
    print('Recall = {}'.format(recall))
    print('F1 = {}'.format(f1))

    with open('preds_78.txt', 'w') as f:
        [f.write('{}\t{}\t{}\n'.format(*t)) for t in results]


if __name__ == '__main__':
    main()