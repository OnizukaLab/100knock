from p30 import read_data
from collections import Counter
import matplotlib.pyplot as pl

dummy = {'surface': '', 'base': '', 'pos': '', 'pos2': ''}

affix = list(map(lambda x : x[0] if len(x) != 0 else dummy, read_data()))

words = [x['surface'] for x in affix if x['pos'] != '記号' and x['surface'] != '']
best10 = list(Counter(words).most_common()[:10])


pl.bar([x for x in range(10)], [x[1] for x in best10])
pl.xticks(range(10), [x[0] for x in best10])
pl.show()
