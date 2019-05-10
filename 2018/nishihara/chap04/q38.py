# coding: UTF-8

from collections import defaultdict
from matplotlib import pyplot as plt
import q30, q36

def q38():
    hdict = defaultdict(int)

    mor = q30.readma("../../../data/neko.txt.mecab")
    wdict = q36.mor2wdict(mor)

    for v in wdict.values():
        hdict[v] += 1

    return sorted(hdict.items(), key=lambda x: -x[1])


if __name__ == '__main__':
    rst = q38()
    plt.bar([t[0] for t in rst], [t[1] for t in rst], align="center")
    plt.xlabel("出現頻度")
    plt.ylabel("出現頻度をとる単語の種類数")
    plt.show()
