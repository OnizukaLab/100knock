from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
import numpy as np
from q_72 import *

def eval_(pred_list, target_list):
    count = [0, 0, 0, 0]  # TN, FP, FN, TP
    for p,t in zip(pred_list, target_list):
        count[t*2+p] += 1
    accuracy = (count[0]+count[3])/sum(count)
    precision = count[3]/(count[1]+count[3])
    recall = count[3]/(count[2]+count[3])
    f_measure = 2*precision*recall/(precision+recall)
    return accuracy, precision, recall, f_measure

if __name__ == '__main__':
    target_list = []
    input_list = []
    with open('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt') as f:
        for line in f:
            l = line.strip()
            target_list.append(1 if l[:2] == '+1' else 0)
            input_list.append(seq2feat(l[3:]))

    def lr_(train_input, train_target, test_input, test_target):
        lr = LogisticRegression()
        lr.fit(train_input, train_target)
        test_pred = lr.predict(test_input)

        return eval_(test_pred, test_target)

    kfold = KFold(n_splits=5, shuffle=True, random_state=0)
    result = [[] for _ in range(4)]
    print('acc\tpre\trec\tf')
    for train_idx, test_idx in kfold.split(input_list):
        train_input, train_target = [input_list[i] for i in train_idx], [target_list[i] for i in train_idx]
        test_input, test_target = [input_list[i] for i in test_idx], [target_list[i] for i in test_idx]
        acc,pre,rec,fm = lr_(train_input, train_target, test_input, test_target)
        result[0].append(acc)
        result[1].append(pre)
        result[2].append(rec)
        result[3].append(fm)
        print('{:.3}\t{:.3}\t{:.3}\t{:.3}'.format(acc, pre, rec, fm))
    print('--------------------')
    print('{:.3}\t{:.3}\t{:.3}\t{:.3}'.format(np.mean(result[0]), np.mean(result[1]), np.mean(result[2]), np.mean(result[3])))
