from q_73 import *

if __name__ == '__main__':
    neg_seq = 'two badly interlocked stories drowned by all too clever complexity .'
    pos_seq = 'the beauty of alexander payne\'s ode to the everyman is in the details .'
    x = [seq2feat(neg_seq),seq2feat(pos_seq)]

    for l,p in zip(lr.predict(x), lr.predict_proba(x)):
        label = '+1' if l == 1 else '-1'
        proba = p[l]
        print(label,proba)
