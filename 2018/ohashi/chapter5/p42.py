from p41 import Chunk, get_chunks

text = get_chunks()

for chunks in text:
    [print('{}\t{}'.format(chunks[i].get_sentence(remove=True), chunks[x].get_sentence(remove=True)))\
     for i, x in enumerate([x.dst for x in chunks]) if x != -1]

