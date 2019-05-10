import re

sentences = []
with open('../../../data/nlp.txt', mode='r') as f:
    sentences.extend(re.split(r'[.;:?!]\s+(?=[A-Z])', f.read().strip()))

if __name__ == '__main__':
    for sentence in sentences:
        print(sentence)
