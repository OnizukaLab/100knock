from q53 import *


class Token():
    """Token"""
    def __init__(self, tokentag):
        for token in tokentag:
            if(token.tag == "word"): self.word = token.text
            elif(token.tag == "lemma"): self.lemma = token.text
            elif(token.tag == "CharacterOffsetBegin"): self.begin = token.text
            elif(token.tag == "CharacterOffsetEnd"): self.end = token.text
            elif(token.tag == "POS"): self.pos = token.text
            elif(token.tag == "NER"): self.ner = token.text
            elif(token.tag == "Speaker"): self.speaker = token.text

    def __str__(self):
        return "\t".join([self.word, self.lemma, self.begin, self.end, self.pos, self.ner, self.speaker])


if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    for tokens in root.findall(".//tokens"):
        for token in tokens:
            t = Token(token)
            print(t.word, t.lemma, t.pos, sep="\t")
