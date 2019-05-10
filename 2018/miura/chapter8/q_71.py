from collections import Counter

counter = Counter()
with open('../../../data/rt-polaritydata/rt-polaritydata/sentiment.txt') as f:
    for line in f:
        counter += Counter(line[3:].strip().split())

stop_list = [c[0] for c in counter.most_common(100)]

def isstop(word):
    return word in stop_list

if __name__ == '__main__':
    # test
    def test_isstop(word, expect):
        result = isstop(word)
        print('{}\treturn:{}\texpect:{}\t->\t{}'.format(word, result, expect, 'OK' if result==expect else 'NG'))

    test_isstop('a', True)
    test_isstop('the', True)
    test_isstop('tired', False)
    test_isstop('great', False)
