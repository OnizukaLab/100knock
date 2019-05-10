from q41 import getChunks

if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        for c in s:
            if(c.dst != -1):
                src = [m.pos for m in c.morphs]
                dst = [m.pos for m in s[c.dst].morphs]
                if("名詞" in src and "動詞" in dst):
                    print(c.get_surface() + "\t" + s[c.dst].get_surface())
