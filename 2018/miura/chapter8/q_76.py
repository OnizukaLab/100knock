from q_73 import *
import numpy as np

# usage : python q_76.py > q_76.out

if __name__ == '__main__':
    input_list,target_list = load_data('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt')
    target_list = [1 if l == '+1' else 0  for l in target_list]
    output_list = lr.predict_proba(input_list)
    for t,o in zip(target_list, output_list):
        print('{}\t{}\t{}'.format(t, np.argmax(o), max(o)))
