from collections import Counter
import pickle

if __name__ == '__main__':
    tc_counter = Counter()
    t_counter = Counter()
    c_counter = Counter()
    tc_list = []
    t_list = []
    c_list = []

    with open('../../../data/enwikidata/k82.txt','r') as data_f:
        data = data_f.read().split('\n')
        data.remove('')
        for idx,line in enumerate(data,1):
            tokens = line.split('\t')
            tc_list.append(line)
            t_list.append(tokens[0])
            c_list.append(tokens[1])

            if idx % 1000000 == 0:
                tc_counter.update(tc_list)
                t_counter.update(t_list)
                c_counter.update(c_counter)
                tc_list = []
                t_list = []
                c_list = []
                print('{} has done...'.format(idx))

    tc_counter.update(tc_list)
    t_counter.update(t_list)
    c_counter.update(c_counter)

    with open('tc_result.pkl','wb') as tc_out:
        pickle.dump(tc_counter,tc_out)
    with open('t_result.pkl','wb') as t_out:
        pickle.dump(t_counter,t_out)
    with open('c_result.pkl','wb') as c_out:
        pickle.dump(c_counter,c_out)
    print('N:{}'.format(idx))
