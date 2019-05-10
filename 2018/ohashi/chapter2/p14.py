import sys

n, filepath = sys.argv[-2:]

with open(filepath, encoding='utf-8') as f:
    for _ in range(int(n)):
        print(next(f).replace('\n', ''))
