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
                for m in zip(s[src].morphs, s[src].morphs[1:]):
                    if m[1].pos == "助詞":
                        p.append((m[0], m[1].base, s[src].get_surface()))
            for e in p:
                if e[0].pos1 == "サ変接続" and e[1] == "を":
                    v = e[2] + v
                    p.remove(e)
                    break
            else:
                continue
            if(len(p) > 0):
                p.sort(key=lambda x: (x[1], x[2]))
                par = [ps[1] for ps in p]
                sur = [ps[2] for ps in p]
                print("{}\t{}\t{}".format(v, " ".join(par), " ".join(sur)))
