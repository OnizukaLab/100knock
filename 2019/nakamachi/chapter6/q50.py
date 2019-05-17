import re

import sys
from os import path
sys.path.append(path.abspath(path.curdir))
from data_loader import data_loader


def sentence_splitter(passage):
    regex = re.compile(r"[.;:?!]\s[A-Z]")
    delimiters = [i.start() for i in regex.finditer(passage)]
    sentence = list()
    current = 0
    for delimiter in delimiters:
        sentence.append(passage[current: delimiter + 1])
        current = delimiter + 2
    sentence.append(passage[current:])
    return sentence


def main():
    passage = data_loader()
    return sentence_splitter(passage)


if __name__ == '__main__':
    print(main())
