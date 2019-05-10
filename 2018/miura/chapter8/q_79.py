import matplotlib.pyplot as plt
from q_73 import *
from q_78 import eval_

def pred_label(pred_list, threshold=0.5):
    return [1 if p[1] > threshold else 0 for p in pred_list]

if __name__ == '__main__':
    input_list,target_list = load_data('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt')
    target_list = [1 if l == '+1' else 0  for l in target_list]
    output_list = lr.predict_proba(input_list)
    pre_list = []
    rec_list = []
    x_list = []
    for t in range(5, 100, 5):
        threshold = t*0.01
        pred_list = pred_label(output_list, threshold=threshold)
        _,pre,rec,_ = eval_(pred_list, target_list)
        pre_list.append(pre)
        rec_list.append(rec)
        x_list.append(threshold)

    '''
    plt.plot(x_list, pre_list, marker='o', label='precision')
    plt.plot(x_list, rec_list, marker='o', label='recall')
    plt.legend(loc='lower left')
    plt.title('Recall and Precision', fontsize=20)
    plt.xlabel('threshold', fontsize=16)
    plt.tick_params(labelsize=14)
    plt.grid(True)
    plt.show()
    '''
    plt.plot(rec_list, pre_list, marker='o')
    plt.title('Recall-Precision Curve', fontsize=20)
    plt.xlabel('recall', fontsize=16)
    plt.ylabel('precision', fontsize=16)
    plt.tick_params(labelsize=14)
    plt.grid(True)
    plt.show()
