from xml.etree.ElementTree import *
import re
from functools import update_wrapper
import itertools

edges = {}


def makeTree(line):
    count = 0; buf = 0; old = 0
    ret = []
    if not re.match('^\(|\)$', line): return line
    for i, c in enumerate(line):
        if c == '(': count += 1
        elif c == ')': count -= 1

        if old == 1 and count == 0:
            ret.append(line[buf:i+1])
            buf = i
        if count == 0:
            buf = i

        old = count
    ret = [re.sub('^\(|\)$|^\s+\(', '', x) for x in ret]

    return [[x.split(' ', 1)[0], makeTree(x.split(' ', 1)[-1])] for x in ret]

def printNP(tree):
    if list in list(map(type, tree)):
        tmp = ' '.join([printNP(t) for t in tree])
        if tree[0] == 'NP': print(re.sub('\s+', ' ', tmp))
        return tmp
    elif type(tree) == str:
        return tree if len(set(list(map(lambda x: x.isupper(), [x for x in tree])))) != 1 else ''
    else:
        if tree[0] == 'NP': print(tree[-1])
        return tree[-1]



def getTerminate(element):
    if element.tag == 'parse':
        printNP(makeTree(element.text))

    return [getTerminate(c) for c in element]

tree = parse('nlp/nlp.txt.xml')

getTerminate(tree.getroot())