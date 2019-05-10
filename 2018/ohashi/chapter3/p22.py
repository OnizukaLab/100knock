import json
import re
import string
from p20 import get_britain



fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp)

fp.close()

for line in re.findall('(.+Category:.+)', text):
    print(re.sub('[{}]'.format(string.punctuation), '', line.split(':')[-1]))