from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)

db = client.test

collection = db.test_collection

print(collection.count({'area': 'Japan'}))