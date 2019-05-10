import redis
import json
import gzip

r = redis.Redis(host='localhost',port=6379,db=1)

with gzip.open('../../../data/artist.json.gz', 'r') as f:
	for line in f:
		obj = json.loads(line)
		if 'tags' in obj:
			r.set(obj['name'], obj['tags'])

print(r.get('Queen').decode('utf-8'))
