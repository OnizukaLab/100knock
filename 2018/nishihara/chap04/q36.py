from collections import defaultdict
import q30

def mor2wdict(mor):
    wdict = defaultdict(int)
    for s in mor:
        for m in s:
            wdict[(m["base"], m["pos"])] += 1
    return wdict

if __name__ == '__main__':
    mor = q30.readma("../../../data/neko.txt.mecab")
    wdict = mor2wdict(mor)

    rst = sorted(wdict.items(), key=lambda x: -x[1])
    for t in rst:
        print(t[1], t[0][0])
