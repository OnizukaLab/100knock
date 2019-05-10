from q_41 import *

for chunks in allsentence:
    for chunk in chunks:
        if not chunk.in_noun(): continue
        print(chunk.surface(), end='')
        dst = chunk.dst
        while dst != -1:
            print(' -> ' + chunks[dst].surface(), end='')
            dst = chunks[dst].dst
        print('')
