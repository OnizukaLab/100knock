from q41 import getChunks
from collections import defaultdict

if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        for c in s:
            v = ""
            p = []
            for m in c.morphs:
                if(m.pos == "動詞"):
                    v = m.base
                    break
            else:
                continue
            for src in c.srcs:
                for m in s[src].morphs:
                    if m.pos == "助詞":
                        p.append((m.base, s[src].get_surface()))
            if(len(p) > 0):
                p.sort()
                par = [ps[0] for ps in p]
                sur = [ps[1] for ps in p]
                print("{}\t{}\t{}".format(v, " ".join(par), " ".join(sur)))
