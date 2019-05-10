import pymongo

client = pymongo.MongoClient()
db = client['nlp100knock_db']
collection = db['artist_collection']

for obj in collection.find({'name':'Queen'}):
    print(obj)
