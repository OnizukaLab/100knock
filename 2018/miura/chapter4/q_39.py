from q_36 import *
import matplotlib.pyplot as plt

#日本語表示用
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

l = [list(x) for x in zip(*counter.most_common(1000))]
plt.loglog(range(1000), l[1])
plt.show()
