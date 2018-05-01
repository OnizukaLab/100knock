import json
import re

def get_britain(fp):
    text = {i: json.loads(line) for i, line in enumerate(fp)}

    return next((text[i]['text'] for i in range(len(text)) if text[i]['title'] == "イギリス"))


fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp).replace('\n', '')


basic = re.findall('{{基礎情報\s国(\|[^{}]+\=([^{}]+|((\**)?{{[^{}]+}}[^{}]*)+)+)+}}', text)
basic = basic[0][0]

info = {}
for var, arg in zip(re.findall('[^\|]+\s\=', basic), re.split('[^\|]+\s\=', basic)[1:]):
    info[re.sub('\s\=\s?', '', var)] = re.sub('\|$', '', arg)

for key in info.keys():
    info[key] = re.sub("'+", '', info[key])
    info[key] = re.sub('\[\[|\]\]|{{|}}|</ref>|<ref\s[^/>]+/>', '', info[key])
    info[key] = re.sub('<ref>|<br/>', '\n', info[key])
    info[key] = re.sub('\*', ' ', info[key])
    print(key, info[key])