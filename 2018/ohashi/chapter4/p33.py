from p30 import read_data
dummy = {'surface': '', 'base': '', 'pos': '', 'pos2': ''}

affix = list(map(lambda x : x[0] if len(x) != 0 else dummy, read_data()))

[print(x['surface']) for x in affix if x['pos'] == '名詞' and x['pos2'] == 'サ変接続']