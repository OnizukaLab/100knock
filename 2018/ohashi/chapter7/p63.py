import plyvel
import json
import os

db = plyvel.DB('artist_tag.ldb', create_if_missing=True)


with open('artist.json', encoding='utf-8') as f:
    tmp = [json.loads(x) for x in f]

for t in tmp:
    try:
        db.put(bytes(t['name'].encode('utf-8')), bytes(json.dumps(t['tags']).encode('utf-8')))
    except:
        db.put(bytes(t['name'].encode('utf-8')), bytes('UNK'.encode('utf-8')))


print(json.loads(db.get(bytes('Linkin Park'.encode('utf-8'))).decode('utf-8')))