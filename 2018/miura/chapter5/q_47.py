from q_41 import *

for chunks in allsentence:
    for i,chunk in enumerate(chunks):
        #サ変接続名詞+を の文節を探す
        sahen = chunk.sahen_wo()
        if sahen is None: continue

        #サ変接続名詞+を の文節が係る文節
        predicate = chunks[chunk.dst]

        vl = predicate.verb_list()
        if len(vl) == 0: continue
        tail = []
        for src in predicate.srcs:
            if src == i: continue #もとのサ変接続名詞の文節を無視する
            pl = chunks[src].particle_list()
            if len(pl) == 0: continue
            tail.append([pl[-1].base, chunks[src].surface()])
        if len(tail) == 0: continue
        #辞書順にする
        tail = sorted(tail)
        print('{}を{}\t{}\t{}'.format(sahen.base, vl[0].base, ' '.join(w[0] for w in tail), ' '.join(w[1] for w in tail)))
