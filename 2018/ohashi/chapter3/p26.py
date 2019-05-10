import json
import re
from p20 import get_britain



fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp).replace('\n', '')


basic = re.findall('{{基礎情報\s国(\|[^{}]+\=([^{}]+|((\**)?{{[^{}]+}}[^{}]*)+)+)+}}', text)
basic = basic[0][0]

info = {}
for var, arg in zip(re.findall('[^\|]+\s\=', basic), re.split('[^\|]+\s\=', basic)[1:]):
    info[re.sub('\s\=\s?', '', var)] = re.sub('\|$', '', arg)

for key in info.keys():
    info[key] = re.sub("'+", '', info[key])
    print(key, info[key])