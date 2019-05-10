from matplotlib import pyplot as plt
import q30, q36

mor = q30.readma("../../../data/neko.txt.mecab")
wdict = q36.mor2wdict(mor)
rst = sorted(wdict.items(), key=lambda x: -x[1])[:10]

plt.bar([t[0][0] for t in rst], [t[1] for t in rst], align="center")
plt.xlabel("単語")
plt.ylabel("出現頻度")
plt.show()
