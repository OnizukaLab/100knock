import re


def read_data():
    sentence = []
    with open('neko.txt.mecab', encoding='utf-8') as f:
        tmp = []
        for line_ in f:
            if line_.find('EOS') == -1 and line_ != '':
                affix = re.split('\s|\t|,', line_.replace('EOS\n', ''))
                tmp.append({'surface': affix[0],
                             'base'   : affix[-4],
                             'pos'    : affix[1],
                             'pos2'   : affix[2]})
            else:
                sentence.append(tmp)
                tmp = []

    return sentence

if __name__ == '__main__':
    print(read_data()[2])