from q53 import *


def xml2dict(xml):
    d = {}
    for e in xml:
        d[e.tag] = e.text
    return d

if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    sentences = [[w[0].text for w in s[0]] for s in root[0][1]]

    for coreference in root[0][2]:
        rep = xml2dict(coreference[0])
        for mention in coreference[1:]:
            m = xml2dict(mention)
            s = int(m["sentence"]) - 1
            start = int(m["start"]) - 1
            end = int(m["end"])
            sentences[s][start] = "{}({})".format(rep["text"], m["text"])
            sentences[s][start + 1:end] = ""

    for s in sentences:
        print(*s, sep='\n')