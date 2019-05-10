from xml.etree.ElementTree import *
import inspect
order = ['word', 'lemma', 'POS']

with open('nlp.txt') as f:
    nlp_text = ''.join(f.readlines())


def getTerminate(element):
    if element.tag == 'coreference':
        try:
            tmp = next(e for e in element if e.keys() == ['representative'])
            rep = next(t for t in tmp if t.tag == 'text').text
            print(['{}({})'.format(rep, e.getchildren()[-1].text) for e in element if e.keys() != ['representative']])
        except: pass

    return [getTerminate(c) for c in element]



tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())
