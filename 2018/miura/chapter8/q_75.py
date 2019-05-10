from q_73 import *

if __name__ == '__main__':
    weight = [(i,c) for i,c in enumerate(lr.coef_[0])]
    weight = sorted(weight, key=lambda x: x[1], reverse=True)
    print('重みの高い素性')
    for i,w in weight[:10]:
        print('{}\t{}'.format(w, feature_list[i]))
    print('重みの低い素性')
    for i,w in weight[-10:]:
        print('{}\t{}'.format(w, feature_list[i]))
