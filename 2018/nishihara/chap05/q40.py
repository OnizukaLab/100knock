# 係り受け解析
# cabocha -f3 neko.txt -o neko.txt.cabocha

import xml.etree.ElementTree as ET

class Morph:
    """形態素を表すクラス"""
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # (surface,base,pos,pos1)
    def __str__(self):
        return "(" + ",".join([self.surface, self.base, self.pos, self.pos1]) + ")"


def readXML(path):
    with open(path) as f:
        XmlData = f.read()
    return ET.fromstring("<root>{}.</root>".format(XmlData))


def getbpp(mecabstr):
    s = mecabstr.split(",")
    return (s[6], s[0], s[1])


if __name__ == '__main__':
    print("\n".join([str(t) for t in [[Morph(t.text, *getbpp(t.get("feature"))) for c in s for t in c] for s in readXML("../../../data/neko.txt.cabocha")][2]]))


    # 下記と等価
    #
    # root = readXML("../../../data/neko.txt.cabocha")
    # rst = []
    # for s in root:
    #     sentence = []
    #     for c in s:
    #         for t in c:
    #             a = t.get("feature").split(",")
    #             sentence.append(Morph(t.text, a[6], a[0], a[1]))
    #     rst.append(sentence)
    #
    # for t in rst[2]:
    #     print(t)