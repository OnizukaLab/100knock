from q41 import getChunks

if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        for c in s:
            if(c.dst != -1):
                print(c.get_surface() + "\t" + s[c.dst].get_surface())
