from p30 import read_data
import numpy as np

for line in read_data():
    flag = ''.join(['1' if x['pos'] == '名詞' else '0' for x in line]).split('0')
    flag = list(map(lambda x : len(x), flag))

    index = np.argmax(flag)

    if flag[index] > 1:
        tar = sum(flag[:index]) + index
        print(''.join([x['surface'] for x in line[tar:tar+flag[index]]]))
