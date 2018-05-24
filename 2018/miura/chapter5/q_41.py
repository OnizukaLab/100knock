from q_40 import *

class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def add_morphs(self, morph):
        self.morphs.append(morph)

    def add_srcs(self, src):
        self.srcs.append(src)

    #そのchunkの表層系を返す。’、。「」’は出力しない。
    def surface(self):
        return ''.join(re.sub(r'[、。「」]', '', morph.surface) for morph in self.morphs)

    #名詞を含むかどうか -> q_43
    def in_noun(self):
        for morph in self.morphs:
            if morph.pos == '名詞': return True
        return False

    #動詞を含むかどうか -> q_43
    def in_verb(self):
        for morph in self.morphs:
            if morph.pos == '動詞': return True
        return False

allsentence = []
chunks = []
now_chunk = None
with open('../../../data/neko.txt.cabocha', mode='r') as f:
    for line in f:
        line = line.strip('\n')
        if line == 'EOS':
            if now_chunk is not None:
                #前のチャンクを閉じる
                chunks.append(now_chunk)
            #srcsをまとめて更新する
            for i,chunk in enumerate(chunks):
                if chunk.dst == -1: continue
                chunks[chunk.dst].add_srcs(i)
            #chunksを閉じる
            allsentence.append(chunks)
            #次のchunksの準備
            chunks = []
            now_chunk = None
        elif re.match(r'\*' ,line):
            if now_chunk is not None:
                #前のchunkを閉じる
                chunks.append(now_chunk)
            #次のchunkの準備
            now_chunk = Chunk(int(line.split(' ')[2][:-1]))
        else:
            # ChunkにMorphを追加する
            now_chunk.add_morphs(Morph(makemorphmap(line)))

if __name__ == '__main__':
    for chunk in allsentence[7]:
        print("{} -> {}".format(chunk.surface(), chunk.dst))
