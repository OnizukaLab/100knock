from q53 import *

if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    for deps in root.findall(".//dependencies[@type='collapsed-dependencies']"):
        for n in deps:
            if(n.get("type") == "nsubj"):
                for d in deps:
                    if(d.get("type") == "dobj"):
                        if(n[0].get("idx") == d[0].get("idx")):
                            print(n[1].text, n[0].text, d[1].text, sep='\t')
