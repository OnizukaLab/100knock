import re
import sys
from os import path

sys.path.append(path.abspath(path.curdir))
from q50 import main as solution


def sentence_list_to_word_list(sentence_list):
    regex = re.compile(r"\s+|[.;:?!]$")
    words = list()
    for sentence in sentence_list:
        words += regex.split(sentence)
    return words


def main():
    solution_50 = solution()
    return sentence_list_to_word_list(solution_50)


if __name__ == '__main__':
    print(main())
