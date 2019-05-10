from q_72 import *
import sklearn
from sklearn.linear_model import LogisticRegression

def load_data(path):
    target_list = []
    input_list = []
    with open(path) as f:
        for line in f:
            l = line.strip()
            target_list.append(l[:2])
            input_list.append(seq2feat(l[3:]))
    return input_list,target_list

input_list,target_list = load_data('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt')
target_list = [1 if l == '+1' else 0  for l in target_list]
lr = LogisticRegression()
lr.fit(input_list, target_list)
