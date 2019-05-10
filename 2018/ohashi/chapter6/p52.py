from nltk.stem import PorterStemmer
from string import punctuation
import re

tokenizer = PorterStemmer()

while True:
    try: buf = re.sub('[{}]'.format(punctuation), '', input())
    except: break
    print('\t'.join([buf, tokenizer.stem(buf)]))


