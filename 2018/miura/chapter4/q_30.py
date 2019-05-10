
def makeWordMap(line):
    if line == 'EOS':
        return None
    words = line.split('\t')
    pos = ['']*5
    for i,c in enumerate(words[3].split('-')): pos[i] = c
    return {'surface': words[0], 'base':words[2], 'pos':pos[0], 'pos1':pos[1]}

allsentence = []
sentence = []
with open('../../../data/neko.txt.mecab', mode='r') as f:
    for line in f:
        line = line.strip('\n')
        if line == 'EOS':
            allsentence.append(sentence)
            sentence = []
            continue
        sentence.append(makeWordMap(line))

if __name__ == '__main__':
    for sentence in allsentence[0:20]:
        print(sentence)
