from q_28 import *
import requests
import json

params = {'action': 'query',
            'format': 'json',
            'titles': 'File:'+basic_dict['国旗画像'],
            'prop': 'imageinfo',
            'iiprop': 'url',
            'iiurlwidth': '220'}
response = requests.get('https://www.mediawiki.org/w/api.php', params = params)
response_json = json.loads(response.text)
print(response_json['query']['pages']['-1']['imageinfo'][0]['url'])
