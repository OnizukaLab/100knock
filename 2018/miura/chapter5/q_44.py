import CaboCha
from graphviz import Digraph
import sys
import re
import pydot

s = input('> ') if len(sys.argv) < 2 else sys.argv[1]

cabocha = CaboCha.Parser()
lattice = cabocha.parse(s).toString(CaboCha.FORMAT_LATTICE)
#print(lattice)

#q_41.py の Chunkはリッチすぎるので簡単なのつくる
class Chunk:
    def __init__(self, dst, surface):
        self.dst = dst
        self.surface = surface

allsentence = []
chunks = []
now_chunk = {'surface':'', 'dst':None}
for line in lattice.split('\n'):
    if line == 'EOS':
        chunks.append(Chunk(**now_chunk))
        now_chunk = {'surface':'', 'dst':None}
        allsentence.append(chunks)
        chunks = []
    elif re.match(r'^\*', line):
        if now_chunk['dst'] is not None:
            chunks.append(Chunk(**now_chunk))
        now_chunk = {'surface':'', 'dst':int(line.split(' ')[2][:-1])}
    else:
        now_chunk['surface'] += re.split(r'[,\t]', line)[0]

#有効グラフをつくる
G = Digraph(format='png')
G.attr('node', shape='oval')
for i,chunks in enumerate(allsentence):
    for j,chunk in enumerate(chunks):
    	G.node('{}-{}'.format(i,j), chunk.surface)
    	if chunk.dst != -1:
    		G.edge('{}-{}'.format(i,j), '{}-{}'.format(i,chunk.dst))

G.render('graph')
