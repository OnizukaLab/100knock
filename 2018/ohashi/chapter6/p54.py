from xml.etree.ElementTree import *
import inspect

order = ['word', 'lemma', 'POS']

def getTerminate(element):
    if element.tag == 'token':
        print('\t'.join(map(lambda x : x.text, sorted([c for c in element if c.tag in order], key=lambda x : order.index(x.tag)))))
    else:
        return [getTerminate(c) for c in element]


tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())