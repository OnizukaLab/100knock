import pymongo
import json
import gzip


client = pymongo.MongoClient()
db = client['nlp100knock_db']
collection = db['artist_collection']

with gzip.open('../../../data/artist.json.gz','r') as f:
	for line in f:
		collection.insert_one(json.loads(line))

# make index
collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
