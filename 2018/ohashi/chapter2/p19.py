from collections import Counter

with open('hightemp.txt', encoding='utf-8') as f:
    lines = [x for x in f]

words = [x.split()[0] for x in lines]
count = list(Counter(words).most_common())

for l in count:
    print(l[0])