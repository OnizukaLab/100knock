from pymongo import MongoClient
import pymongo
import json


client = MongoClient('localhost', 27017)

db = client.test

collection = db.test_collection

cursors = collection.find({'tags.value': 'dance'}).sort('tags.value', pymongo.DESCENDING)

[print(d) for d in cursors[:10]]