from q41 import getChunks

if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        for c in s:
            if("名詞" in [m.pos for m in c.morphs]):
                p = []
                ch = c
                while True:
                    p.append(ch.get_surface())
                    if ch.dst == -1:
                        break
                    ch = s[ch.dst]
                print(" -> ".join(p))