import redis
r = redis.Redis(host='localhost',port=6379,db=0)

def get(s):
	return r.get(s).decode('utf-8')

if __name__ == '__main__':
	print(get('Jamz'))
