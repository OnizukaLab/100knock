from p41 import Chunk, get_chunks

text = list(filter([].__ne__, get_chunks()))

index = 10

V = list(filter(lambda x : '動詞' in x.get_pos_list(), text[index]))
P = [sum(([x.base for x in text[index][y].morphs if x.pos == '助詞'] for y in v.srcs), []) for v in V]

V = list(map(lambda x : next(y.base for y in x.morphs if y.pos == "動詞"), V))

for v, p in zip(V, P):
    print('\t'.join([v] + [q for q in p]))


