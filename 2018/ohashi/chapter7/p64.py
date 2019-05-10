from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)

db = client.test

collection = db.test_collection

'''
with open('artist.json', encoding='utf-8') as f:
    tmp = [json.loads(x) for x in f]

for j in tmp[:10]:
    collection.insert_one(j)
'''

collection.create_index([('aliases.name', 1)], name='aliases.name')

