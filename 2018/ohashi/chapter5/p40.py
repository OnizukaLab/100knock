import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __getitem__(self, item):
        if item == 'surface': return self.surface
        elif item == 'base': return self.base
        elif item == 'pos': return self.pos
        elif item == 'pos1': return self.pos1
        else: raise KeyError('{} is not exist'.format(item))

    def __setitem__(self, key, value):
        if key == 'surface': self.surface = value
        elif key == 'base': self.base = value
        elif key == 'pos': self.pos = value
        elif key == 'pos1': self.pos1 = value

    def __repr__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)

def create_list(line):
    return [Morph(y[0], y[-3], y[1], y[2]) for y in map(lambda x : re.split('\s|\t|,', x), line)\
                                           if y[0] not in ['*', '']]

if __name__ == '__main__':
    with open('neko.txt.cabocha') as f:
        lines = map(lambda x : re.split('\n', x), ''.join(f.readlines()).split('EOS\n'))

    text = [create_list(line) for line in lines]
    text = list(filter([].__ne__, text))


    print(text[3])





