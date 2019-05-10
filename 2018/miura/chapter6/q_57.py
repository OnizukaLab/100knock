from graphviz import Digraph
from lxml import etree

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    G = Digraph(format='png')
    G.attr('node',shape='oval')

    #1文目をグラフにする
    sentence = root.xpath('//sentence')[0]
    for word in sentence.xpath('tokens/token'):
    	G.node(str(word.attrib['id']), label=word.xpath('word')[0].text)

    for d in sentence.xpath('dependencies[@type="collapsed-dependencies"]/dep'):
    	governor = d.xpath('governor')[0].attrib['idx']
    	dependent = d.xpath('dependent')[0].attrib['idx']
    	G.edge(str(governor),str(dependent))

    print(G)
    G.render('graph_57')
