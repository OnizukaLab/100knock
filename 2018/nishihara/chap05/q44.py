from graphviz import Digraph
from q41 import getChunks


if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    # テストとして初めの10文を書き出す
    for i,s in enumerate(rst[:10]):
        G = Digraph(format='png')
        G.attr('node', shape='circle')
        for c in s:
            if(c.dst != -1):
                G.edge(c.get_surface(), s[c.dst].get_surface())
        G.render("q44/tree{}".format(i))
