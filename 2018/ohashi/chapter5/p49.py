from p41 import Chunk, get_chunks
from p48 import get_path
import itertools

text = list(filter([].__ne__, get_chunks()))

index = 5

norms = [i for i, x in enumerate(text[index]) if '名詞' in x.get_pos_list()]

for a, b in itertools.combinations(norms, 2):
    pa = get_path(text[index], text[index][a], morph=True)
    pb = get_path(text[index], text[index][b], morph=True)
    pivot = min(list(set(pa) & set(pb)), key=pa.index)
    path = [[], []]
    path[0] = next(pa[:i] for i in range(1, len(pa)+1) if pa[i-1] == pivot)
    path[1] = next(pb[:i] for i in range(1, len(pb)+1) if pb[i-1] == pivot)

    #print(path)

    path[0][0].replace(['pos', '名詞'], ['surface', 'X'], 1)
    path[1][0].replace(['pos', '名詞'], ['surface', 'Y'], 1)

    if len(path[1]) > 1: print(' -> '.join([x.get_sentence() for x in path[0][:-1]]) + ' | ' + \
                               ' -> '.join([x.get_sentence() for x in path[1][:-1]]) + ' | ' + \
                               path[0][-1].get_sentence())
    else:
        print(' -> '.join([x.get_sentence() for x in path[0][:-1]] + [path[1][-1].get_sentence()]))





