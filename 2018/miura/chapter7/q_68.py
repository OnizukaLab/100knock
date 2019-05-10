import pymongo

client = pymongo.MongoClient()
db = client['nlp100knock_db']
collection = db['artist_collection']

l = collection.find({'tags.value': 'dance'})
l.sort('rating.count', pymongo.DESCENDING)
for obj in l[:10]:
    print(obj)
