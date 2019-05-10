from p30 import read_data


for line in read_data():
    [print(''.join([x['surface'] for x in line[i-1:i+2]])) for i in range(1, len(line)-1)\
                                                           if line[i-1]['pos'] == '名詞' and\
                                                           line[i]['surface'] == 'の' and\
                                                           line[i+1]['pos'] == '名詞']