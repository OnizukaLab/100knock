import re

class Morph:
    def __init__(self, morphmap):
        self.surface = morphmap['surface']
        self.base = morphmap['base']
        self.pos = morphmap['pos']
        self.pos1 = morphmap['pos1']

    def __repr__(self):
        return '{{surface:{} base:{} pos:{} pos1:{}}}'.format(self.surface, self.base, self.pos, self.pos1)

def makemorphmap(string):
    words = re.split(r'[,\t]', string)
    return {'surface':words[0], 'base':words[7], 'pos':words[1], 'pos1':words[2]}

if __name__ == '__main__':
    allsentence = []
    sentence = []
    with open('../../../data/neko.txt.cabocha', mode='r') as f:
        for line in f:
            line = line.strip('\n')
            if re.match(r'\*' ,line):
                pass
            elif line == 'EOS':
                allsentence.append(sentence)
                sentence = []
            else:
                sentence.append(Morph(makemorphmap(line)))

    for w in allsentence[2]: print(w)
