from q_36 import *
import matplotlib.pyplot as plt

#日本語表示用
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

#列と行を入れ替える
l = [list(x) for x in zip(*counter.most_common(10))]
print(l)

plt.bar(range(10), l[1], tick_label=l[0], align='center')
plt.show()
