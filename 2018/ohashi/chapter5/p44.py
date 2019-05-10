from p41 import Chunk, get_chunks

text = list(filter([].__ne__, get_chunks()))

def build_graph(chunks):
    return [[x.get_sentence(), [chunks[y].get_sentence() for y in x.srcs]] for x in chunks if x.get_sentence() != '']


graph = build_graph(text[5])
with open('graph.dot', 'w', encoding='utf-8') as f:
    f.write('digraph foo{\n')
    for list_ in graph:
        [f.write('{} -> {};\n'.format(x, list_[0])) for x in list_[1] if x != '']
    [f.write('{} [fontname="MSゴシック"]\n'.format(x[0])) for x in graph]
    f.write('}')

print(text[5])

