import json
import gzip

def extract(title):
	with gzip.open('../../../data/jawiki-country.json.gz', mode='r') as f:
	for line in f:
		article = json.loads(line.decode('utf-8'))
		if article['title'] == title:
			return article['text']

if __name__ == '__main__':
	print(extract('イギリス'))
