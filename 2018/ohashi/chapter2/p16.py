import sys

n, filepath = sys.argv[-2:]

with open(filepath, encoding='utf-8') as f:
    lines = [x for x in f]

size = int(len(lines) / int(n))

for i in range(int(n) - 1):
    with open('sp{}.txt'.format(i), 'w', encoding='utf-8') as f:
        f.write(''.join(lines[size*i:size*(i+1)]))

with open('sp{}.txt'.format(int(n)), 'w', encoding='utf-8') as f:
    f.write(''.join(lines[size*int(int(n)-1):]))


