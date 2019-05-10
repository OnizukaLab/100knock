from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)

db = client.test

collection = db.test_collection

[print(d) for d in collection.find({'name': 'Queen'})]

print(collection.find_one({'name': 'Queen'}))
collection.update_one({'name': 'Queen'}, {'$set' :{'area': 'Other'}})
print(collection.find_one({'name': 'Queen'}))