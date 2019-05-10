from p30 import read_data
from collections import Counter

dummy = {'surface': '', 'base': '', 'pos': '', 'pos2': ''}

affix = list(map(lambda x : x[0] if len(x) != 0 else dummy, read_data()))

words = [x['surface'] for x in affix if x['pos'] != '記号' and x['surface'] != '']
[print(x) for x in Counter(words).most_common()]