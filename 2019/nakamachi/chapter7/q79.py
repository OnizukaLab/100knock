# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))
import pickle
from sklearn.linear_model import LogisticRegression

from q72 import load_data

MODEL_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/model_cv.pkl"
y_test, X = load_data()

lr = LogisticRegression()
lr.fit(X, y_test)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(lr, f)


def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


y_score = lr.predict(X)
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from inspect import signature

precision, recall, _ = precision_recall_curve(y_test, y_score)

# In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
step_kwargs = ({'step': 'post'}
               if 'step' in signature(plt.fill_between).parameters
               else {})
plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve')
plt.show()
