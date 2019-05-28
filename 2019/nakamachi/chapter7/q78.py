# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))

import pickle
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from q72 import load_data

MODEL_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/model_cv.pkl"
y, X = load_data()

lr = LogisticRegressionCV(cv=5)
lr.fit(X, y)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(lr, f)


def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


y_pred = lr.predict(X)
print("accuracy: %0.4f" % (accuracy_score(y, y_pred)))
print("precision: %0.4f" % (precision_score(y, y_pred)))
print("recall: %0.4f" % (recall_score(y, y_pred)))
print("F-measure:%0.4f" % (f1_score(y, y_pred)))
