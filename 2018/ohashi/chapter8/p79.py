from sklearn.metrics import precision_recall_curve
import pandas as pd
import matplotlib.pyplot as pl

def main():
    df = pd.read_csv('preds_78.txt', sep='\t', header=None)
    true = df.ix[:, 0].values.flatten()
    preds = df.ix[:, 2].values.flatten()

    precision, recall, _ = precision_recall_curve(true, preds, pos_label=1)


    pl.step(recall, precision)
    pl.show()

if __name__ == '__main__':
    main()