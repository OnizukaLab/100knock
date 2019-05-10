# 形態素解析
# $ mecab -F"%m,%f[6],%f[0],%f[1]\n" neko.txt > neko.txt.mecab

def readma(path):
    tpl = ["surface", "base", "pos", "pos1"]

    rst = []
    ln = []
    with open(path, "r") as f:
        for l in f.readlines():
            if("EOS" in l):
                rst.append(ln)
                ln = []
            else:
                ln.append(dict(zip(tpl, l.rstrip().split(","))))
    return rst

if __name__ == '__main__':
    print(readma("../../../data/neko.txt.mecab"))
