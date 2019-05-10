import pymongo

client = pymongo.MongoClient()
db = client['nlp100knock_db']
collection = db['artist_collection']

name = 'Ljiraq'
for obj in collection.find({'aliases.name': name}):
	print(obj)
