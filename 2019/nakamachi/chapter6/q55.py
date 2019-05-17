import sys
from os import path

sys.path.append(path.abspath(path.curdir))
from data_loader import data_loader

root = data_loader(True)

# tokenの抽出
for token in root.iterfind(
    './document/sentences/sentence/tokens/token[NER="PERSON"]'
):
    print(token.findtext('word'))