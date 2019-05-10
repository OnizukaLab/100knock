from matplotlib import pyplot as plt
import q38

rst = q38.q38()

plt.xscale("log")
plt.yscale("log")
plt.xlabel("出現頻度")
plt.ylabel("出現頻度をとる単語の種類数")
plt.scatter([t[0] for t in rst], [t[1] for t in rst])
plt.show()
