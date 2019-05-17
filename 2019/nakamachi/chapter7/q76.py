import sys
from os import path
import csv

sys.path.append(path.abspath(path.curdir))
from q72 import load_data
from q73 import load_model

lr = load_model()
y, X = load_data()

y_hat = list(lr.predict(X))
y_prob = list(lr.predict_proba(X))
y = list(y)

def generate_csv_style_data():
    data = ""
    for idx, grand_truth in enumerate(y):
        data +=",".join([str(x) for x in [grand_truth, y_hat[idx], max(y_prob[idx])]])
        data += "\n"
    return data

if __name__ == '__main__':
    print(generate_csv_style_data())
