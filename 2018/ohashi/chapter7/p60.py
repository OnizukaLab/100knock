import plyvel
import json
import os

db = plyvel.DB('artist_area.ldb', create_if_missing=True)


with open('artist.json', encoding='utf-8') as f:
    tmp = [json.loads(x) for x in f]

for t in tmp:
    try:
        db.put(bytes(t['name'].encode('utf-8')), bytes(t['area'].encode('utf-8')))
    except:
        db.put(bytes(t['name'].encode('utf-8')), bytes('UNK'.encode('utf-8')))


[print(db.get(bytes(tmp[i]['name'].encode('utf-8')))) for i in range(len(tmp))]