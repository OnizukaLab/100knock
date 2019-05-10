import re

with open('nlp.txt') as f:
    text = ''.join(f.readlines()).replace('\n', '')

loc = [x.start() for x in re.finditer('[\.|;|\:|\?|\!]\s[A-Z]', text)]


for a, b in zip([-2,]+loc[:-1], loc[1:]+[len(loc)]):
    print(text[a+2:b])


