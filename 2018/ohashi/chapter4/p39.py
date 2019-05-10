from p30 import read_data
from collections import Counter
import matplotlib.pyplot as pl
import numpy as np

dummy = {'surface': '', 'base': '', 'pos': '', 'pos2': ''}

affix = list(map(lambda x : x[0] if len(x) != 0 else dummy, read_data()))

words = [x['surface'] for x in affix if x['pos'] != '記号' and x['surface'] != '']
count = [x[1] for x in list(Counter(words).most_common())]
hist = list(Counter(count).most_common())


pl.scatter([np.log(x) for x in range(1, len(hist)+1)], [np.log(x[1]) for x in hist])


pl.show()