from xml.etree.ElementTree import *
import inspect
order = ['word', 'lemma', 'POS']

with open('nlp.txt') as f:
    nlp_text = ''.join(f.readlines())


def getTerminate(element):
    if element.tag == 'token':
        if next(e.text for e in element if e.tag == 'NER') == 'PERSON':
            print(next(e.text for e in element if e.tag == 'word'))
    else:
        return [getTerminate(c) for c in element]


tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())

