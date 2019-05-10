import json
import re
import requests
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
    info[key] = re.sub('\[\[|\]\]|{{|}}|</ref>|<ref\s[^/>]+/>', '', info[key])
    info[key] = re.sub('<ref>|<br/>', '\n', info[key])
    info[key] = re.sub('\*', ' ', info[key])

filename = info['国旗画像'][1:]

response = requests.get('https://ja.wikipedia.org/w/api.php?\
                        action=query&titles=File:{}&prop=imageinfo&iiprop=url&format=json'.format(filename))
print(json.loads(response.text)['query']['pages']['-1']['imageinfo'][0]['url'])