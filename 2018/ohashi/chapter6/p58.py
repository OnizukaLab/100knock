from xml.etree.ElementTree import *
import itertools

edges = {}

def printSVO(subtree, root):
    nsubj = list(filter(lambda x : x[0] == 'nsubj', subtree))
    dobj = list(filter(lambda x : x[0] == 'dobj', subtree))

    if len(nsubj)*len(dobj) >= 1:
        for e1, e2 in itertools.product(nsubj, dobj):
            print('{}\t{}\t{}'.format(nsubj[0][1], root, dobj[0][1]))


def getTerminate(element):
    if element.tag == 'dependencies' and element.attrib['type'] == 'collapsed-dependencies':
        global edges
        edges = {}
        #print([[f.text for f in e] + [e.attrib] for e in element])
        for e in element:
            try: edges[e.getchildren()[0].text].append((e.attrib['type'], e.getchildren()[1].text))
            except: edges[e.getchildren()[0].text] = [(e.attrib['type'], e.getchildren()[1].text)]
        del edges['ROOT']

        [printSVO(edges[key], key) for key in edges.keys()]

    return [getTerminate(c) for c in element]

tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())
