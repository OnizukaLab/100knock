from q53 import *
from q54 import *


if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    for tokens in root.findall(".//tokens"):
        for token in tokens:
            t = Token(token)
            if(t.ner == "PERSON"):
                print(t.word)
