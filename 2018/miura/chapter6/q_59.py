from lxml import etree

class node:
    def __init__(self, parent=None, idx=None):
        self.tag = None
        self.parent = parent
        self.idx = idx
        self.child = []
        self.word = []

    def __repr__(self):
        return '{{tag: {}, parent: {}, idx: {}, child: {}, word: {}}}'.format(self.tag, self.parent, self.idx, '['+', '.join([str(c) for c in self.child])+']', '['+', '.join(self.word)+']')

def Sparse(line):
    data = []
    l = line.replace('(','( ').replace(')',' )').split()
    data.append(node(parent=None, idx=0)) #ダミーのroot
    now_idx = 0
    for token in l:
        if token == '(':
            data.append(node(parent=now_idx, idx=len(data)))
            data[now_idx].child.append(len(data)-1)
            now_idx = len(data)-1
            state = '('
        elif token == ')':
            data[data[now_idx].parent].word.extend(data[now_idx].word)
            now_idx = data[now_idx].parent
            state = ')'
        else:
            if state == '(':
                data[now_idx].tag = token
                state = 'tag'
            elif state == 'tag':
                data[now_idx].word.append(token)
            else:
                print('いや、そのりくつはおかしい')
    return data

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    for parse in root.xpath('//parse'):
        tree = Sparse(parse.text)
        for n in tree:
            if n.tag == 'NP':
                print(' '.join(n.word))
