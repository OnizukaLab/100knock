from p41 import Chunk, get_chunks

text = get_chunks()

for chunks in text:
    [print('{}\t{}'.format(x.get_sentence(remove=True), chunks[x.dst].get_sentence(remove=True))) for x in chunks\
     if '名詞' in x.get_pos_list() and '動詞' in chunks[x.dst].get_pos_list()]