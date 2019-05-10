import re


head_pattern = re.compile(r'^[\.\,\!\?\;\:\(\)\[\]]*')
tail_pattern = re.compile(r'[\.\,\!\?\;\:\(\)\[\]]*$')

def rm_token(word):
    tmp = head_pattern.sub('', word)
    word = tail_pattern.sub('', tmp)

    return word

def cleaning(filename, outfile):
    with open(filename, 'r') as f:
        data = f.read().split('\n')
    data = [[rm_token(word) for word in line.split(' ')] for line in data]

    with open(outfile, 'w') as out_f:
        out_f.write('\n'.join([' '.join([word for word in line]) for line in data]))

if __name__ == '__main__':
    ifile = '../../../data/enwikidata/enwiki-20150112-400-r100-10576.txt'
    ofile = '../../../data/enwikidata/chapter9_corpus.txt'
    cleaning(ifile, ofile)
    