from xml.etree.ElementTree import *
import inspect


def getTerminate(element):
    if len(element) == 0:
        if element.tag == 'word': print(element.text)
        return None
    else:
        return [getTerminate(c) for c in element]


tree = parse('nlp/nlp.txt.xml')
getTerminate(tree.getroot())