from q_41 import *

for chunks in allsentence:
    for chunk in chunks:
        if chunk.dst != -1 and chunk.in_noun() and chunks[chunk.dst].in_verb():
            print('{}\t{}'.format(chunk.surface(), chunks[chunk.dst].surface()))
