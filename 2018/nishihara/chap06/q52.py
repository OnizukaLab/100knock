# python3 q50.py | python3 q51.py | python3 q52.py

import sys
from stemming.porter2 import stem

if __name__ == '__main__':
    for line in sys.stdin:
        print(line.strip(), stem(line.strip()), sep='\t')
