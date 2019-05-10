import random

if __name__ == '__main__':
    with open('../../../data/enwikidata/concat_phrase.txt','r') as data_f, \
            open('../../../data/enwikidata/k82.txt','w') as out_f:
            for line in data_f:
                tokens = line.strip().split(' ')
                for i in range(len(tokens)):
                    t = tokens[i]
                    d = random.randint(1,5)

                    for k in range(max(i-d,0),min(i+d,len(tokens))):
                        if i != k:
                            print('{}\t{}'.format(t,tokens[k]),file=out_f)
