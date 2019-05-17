import sys
from os import path

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

sys.path.append(path.abspath(path.curdir))
from q72 import load_data

MODEL_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/model.pkl"
y, X = load_data()

lr = LogisticRegression()
lr.fit(X, y)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(lr, f)


def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

