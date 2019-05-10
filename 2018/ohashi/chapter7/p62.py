import plyvel

db = plyvel.DB('artist_area.ldb')

print(sum(1 if value.decode('utf-8') == 'Japan' else 0 for key, value in db))