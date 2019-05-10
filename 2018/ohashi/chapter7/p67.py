from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)

db = client.test

collection = db.test_collection

cursor = collection.find({'aliases.name': input()})

[print(d) for d in cursor]

