from p40 import Morph, create_list
import re

class Chunk:
    def __init__(self, morph_list):
        try: self.dst = int(morph_list[0].split()[2][0])
        except: self.dst = -1
        morph_list = list(filter(''.__ne__, morph_list))
        self.morphs = [Morph(x[0], x[-3], x[1], x[2]) for x in [re.split('\s|\t|,', y) for y in morph_list[1:]]\
                       if x[0] != '']
        self.srcs = []

    def __getitem__(self, item):
        return self.morphs[item]


    def __repr__(self):
        return '文字列: {}  係り先: {}'.format(''.join([x.surface for x in self.morphs]), self.dst)

    def link(self, n):
        self.srcs.append(n)

    def get_sentence(self, remove=False):
        return (re.sub('。|、|「|」', '', ''.join(x.surface for x in self.morphs))\
                if remove else ''.join(x.surface for x in self.morphs))

    def get_pos_list(self):
        return [x.pos for x in self.morphs]

    def match(self, patten):
        c = 0
        for m in self.morphs:
            if m[patten[c][0]] == patten[c][1]:
                c += 1
            else: c = 0

            if c >= len(patten): break

        return c >= len(patten)

    def find(self, patten):
        return next(m for m in self.morphs if m[patten[0]] == patten[1])

    def replace(self, patten, replace, n):
        m = 0
        for i in range(len(self.morphs)):
            if self.morphs[i][patten[0]] == patten[1]:
                self.morphs[i][replace[0]] = replace[1]
                m += 1
            if m >= n: break


def get_chunks():
    with open('neko.txt.cabocha') as f:
        lines = list(map(lambda x : re.split('\n', x), ''.join(f.readlines()).split('EOS\n')))

    text = []
    for line in lines:
        index = [i for i, x in enumerate(line) if re.match('\*', x)] + [len(line)]

        chunks = [Chunk(line[s:e]) for s, e in zip(index[:-1], index[1:])]
        [chunks[x.dst].link(i) for i, x in enumerate(chunks) if x.dst != -1]

        text.append(chunks)

    return text



if __name__ == '__main__':
    print(get_chunks()[8])
