import sys

n, filepath = sys.argv[-2:]

with open(filepath, encoding='utf-8') as f:
    lines = [x for x in f]

for i in range(int(n)):
    print(lines[-i-1].replace('\n', ''))