from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd

def calc_score(true, preds):
    prec = precision_score(true, preds)
    recall = recall_score(true, preds)
    f1 = f1_score(true, preds)

    return prec, recall, f1


def main(file_name):
    df = pd.read_csv(file_name, sep='\t', header=None)

    label = df.ix[:, 0].apply(lambda x: int(x >= 1)).values.flatten()
    preds = df.ix[:, 1].apply(lambda x: int(x >= 1)).values.flatten()

    prec, recall, f1 = calc_score(label, preds)

    print('Precision = {}'.format(prec))
    print('Recall = {}'.format(recall))
    print('F1 = {}'.format(f1))

if __name__ == '__main__':
    main('preds_76.txt')
