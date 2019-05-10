import plyvel

db = plyvel.DB('artist_area.ldb')

print(db.get(bytes(input().encode('utf-8'))).decode('utf-8'))