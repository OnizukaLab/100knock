import sys
from os import path

sys.path.append(path.abspath(path.curdir))
from data_loader import data_loader


def main():
    root = data_loader(xml_version_flg=True)
    words = list()
    for sentence in root[0][1].getchildren():
        for token in sentence[0].getchildren():
            words.append(token.find("word").text)
    return words


if __name__ == '__main__':
    for item in main():
        print(item)
