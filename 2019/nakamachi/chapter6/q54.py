import sys
from os import path

sys.path.append(path.abspath(path.curdir))
from data_loader import data_loader



root = data_loader(True)

for token in root.iter('token'):
    word = token.findtext('word')
    lemma = token.findtext('lemma')
    pos = token.findtext('POS')
    print('{}\t{}\t{}'.format(word, lemma, pos))