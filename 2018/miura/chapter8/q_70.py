import codecs
import random

def load_data(path, label):
    with codecs.open(path, 'r', 'cp1252') as f:
        return [[label,line.strip()] for line in f]

if __name__ == '__main__':
    data_path = '../../../data/rt-polaritydata/rt-polaritydata/'
    data = load_data(data_path+'rt-polarity.neg', label='-1')
    data += load_data(data_path+'rt-polarity.pos', label='+1')
    random.shuffle(data)
    with open(data_path+'sentiment.txt','w') as f:
        f.write('\n'.join([' '.join(d) for d in data]))

    #count
    neg_count = 0
    pos_count = 0
    with open(data_path+'sentiment.txt', 'r') as f:
        for line in f:
            if line[0:2] == '-1': neg_count += 1
            elif line[0:2] == '+1': pos_count += 1
    print('pos:{} neg:{}'.format(neg_count, pos_count))
