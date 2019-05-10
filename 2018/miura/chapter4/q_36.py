from q_30 import *
import collections

counter = collections.Counter()
for sentence in allsentence:
    counter.update(word['base'] for word in sentence)

if __name__ == '__main__':
    for word in counter.most_common(10):
        print(word)
