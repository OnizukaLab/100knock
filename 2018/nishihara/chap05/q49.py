import itertools
from q41 import getChunks

def to_root(s, chunk):
    p = []
    ch = chunk
    while True:
        p.append(ch)
        if ch.dst == -1:
            break
        ch = s[ch.dst]
    return p


def split_end(list1, list2):
    l1 = list1[::-1]
    l2 = list2[::-1]
    for ls in zip(l1, l2):
        if(ls[0] == ls[1]):
            n = ls[0]
            l1 = l1[1:]
            l2 = l2[1:]
    return (l1[::-1], l2[::-1], n)


def to_xy(morphs, xy):
    for i,m in enumerate(morphs):
        if(m.pos == "名詞"):
            origin = morphs[i].surface
            morphs[i].surface = xy
    return morphs,origin

if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        n = [to_root(s, c) for c in s if("名詞" in [m.pos for m in c.morphs])]
        cs = [c for c in itertools.combinations(n, 2)]
        for c in cs:
            l1,l2,pub = split_end(c[0], c[1])
            l1[0].morphs,o1 = to_xy(l1[0].morphs, "X")
            x = [ch.get_surface() for ch in l1]
            l1[0].morphs,o1 = to_xy(l1[0].morphs, o1)
            if(len(l2) > 0):
                l2[0].morphs,o2 = to_xy(l2[0].morphs, "Y")
                y = [ch.get_surface() for ch in l2]
                l2[0].morphs,o2 = to_xy(l2[0].morphs, o2)
                print(" -> ".join(x), "|", " -> ".join(y), "|", pub.get_surface())
            else:
                y = [ch.get_surface() for ch in l2]
                pub.morphs,o = to_xy(pub.morphs, "Y")
                print(" -> ".join(x), "->", pub.get_surface())
                pub.morphs,o = to_xy(pub.morphs, o)
            # for a in c:
            #     print([b.get_surface() for b in a])
            # print(*[b.get_surface() for b in c[0]])
            # print(*[b.get_surface() for b in c[1]])
        # for c in s:
        #     if("名詞" in [m.pos for m in c.morphs]):
        #         p = []
        #         ch = c
        #         while True:
        #             p.append(ch.get_surface())
        #             if ch.dst == -1:
        #                 break
        #             ch = s[ch.dst]
        #         print(" -> ".join(p))