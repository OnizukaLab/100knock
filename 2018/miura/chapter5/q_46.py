from q_41 import *

for chunks in allsentence:
    for chunk in chunks:
        vl = chunk.verb_list()
        if len(vl) == 0: continue
        tail = []
        for src in chunk.srcs:
            pl = chunks[src].particle_list()
            if len(pl) == 0: continue
            tail.append([pl[-1].base, chunks[src].surface()])
        if len(tail) == 0: continue
        #辞書順にする
        tail = sorted(tail)
        print('{}\t{}\t{}'.format(vl[0].base, ' '.join(w[0] for w in tail), ' '.join(w[1] for w in tail)))
