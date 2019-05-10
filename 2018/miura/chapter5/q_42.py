from q_41 import *

for chunks in allsentence:
    for chunk in chunks:
        if chunk.dst == -1: continue
        print("{}\t{}".format(chunk.surface(),  chunks[chunk.dst].surface()))
