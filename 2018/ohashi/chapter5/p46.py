from p41 import Chunk, get_chunks

text = list(filter([].__ne__, get_chunks()))

index = 10

V = list(filter(lambda x : '動詞' in x.get_pos_list(), text[index]))
P = [sum(([x.base for x in text[index][y].morphs if x.pos == '助詞'] for y in v.srcs), []) for v in V]
S = [[text[index][x].get_sentence() for x in v.srcs if '助詞' in text[index][x].get_pos_list()] for v in V]

V = list(map(lambda x : next(y.base for y in x.morphs if y.pos == "動詞"), V))

for v, p, s in zip(V, P, S):
    if len(p)*len(s) != 0: print('\t'.join([v] + [q for q in p] + [t for t in s]))