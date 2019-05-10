import regex as re
from q53 import *

if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    for parse in root.findall(".//parse"):
        # print(parse.text + "\n")
        # s = re.findall("(\(NP([^()]*\([^()]*\))*\))", parse.text, overlapped=True)
        s = re.findall("((?<rec>\((?:[^()]+|(?&rec))*\)))", parse.text, overlapped=True)
        nps = [l[0] for l in s if(l[0][:4] == "(NP ")]
        for np in nps:
            print(*re.findall("\([^ ()]+ ([^ ()]+)\)", np))
