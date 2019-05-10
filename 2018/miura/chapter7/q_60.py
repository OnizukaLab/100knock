import redis
import json
import gzip

r = redis.Redis(host='localhost',port=6379,db=0)
r.flushall()

with gzip.open('../../../data/artist.json.gz','r') as f:
	for line in f:
		obj = json.loads(line)
		if 'name' in obj and 'area' in obj:
			r.set(obj['name'],obj['area'])
