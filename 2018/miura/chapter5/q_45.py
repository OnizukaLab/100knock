from q_41 import *

for chunks in allsentence:
    for chunk in chunks:
        vl = chunk.verb_list()
        if len(vl) == 0: continue
        tail = []
        for src in chunk.srcs:
            pl = chunks[src].particle_list()
            if len(pl) == 0: continue
            tail.append(pl[0].base)
        if len(tail) == 0: continue
        #辞書順にする
        tail = sorted(tail)
        print('{}\t{}'.format(vl[0].base, ' '.join(tail)))
