from p41 import Chunk, get_chunks

text = list(filter([].__ne__, get_chunks()))

index = 123

for a in text:
    V = list(filter(lambda x : x.match([['pos1', 'サ変接続'], ['surface', 'を']]) and '動詞' in a[x.dst].get_pos_list(), a))

    if len(V):
        phase = [v.get_sentence() + a[v.dst].find(['pos', '動詞'])['base'] for v in V]
        P     =[\
               [a[i] for i in (set(v.srcs) | set(a[v.dst].srcs)) if '助詞' in a[i].get_pos_list() and i not in [v.dst, a.index(v)]]\
                for v in V\
               ]
        Q = [sorted([q.find(['pos', '助詞'])['base'] for q in p]) for p in P]
        [p.sort(key=lambda x: x.find(['pos', '助詞'])['base']) for p in P]

        print(['{}  '.format(x)+' '.join(z)+'   '+' '.join([a.get_sentence(remove=True) for a in y ]) for x, y, z in zip(phase, P, Q)])




