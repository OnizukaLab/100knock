from xml.etree.ElementTree import *
import re
from string import punctuation
import inspect
order = ['word', 'lemma', 'POS']
I = 0

with open('nlp.txt') as f:
    nlp_text = ''.join(f.readlines())

def makeDOT(tree, index):
    with open('tree{}.dot'.format(index), 'w') as f:
        f.write('digraph tree' + str(index) + ' {\n')
        [f.write(' -> '.join([re.sub('[{}]'.format(punctuation), 'S', f.text) for f in e.getchildren()]) + ';\n') for e in tree]
        f.write('}')



def getTerminate(element):
    global I
    if element.tag == 'dependencies' and element.attrib['type'] == 'collapsed-dependencies':
        makeDOT(element, I)
        I += 1
    return [getTerminate(c) for c in element]

tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())