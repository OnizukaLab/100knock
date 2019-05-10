import json
import re
import string
from p20 import get_britain



fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp)

fp.close()

for line in re.findall('(<ref>.+</ref>)', text):
    line = re.sub('(<ref>|</ref>|)', '', line)
    for ref in re.findall('http[a-zA-Z{}]+'.format(string.punctuation), line): print(ref)

