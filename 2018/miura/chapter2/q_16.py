import sys

if len(sys.argv) < 3:
	print('usage: python q_16.py <filename> <number>')
else:
	with open(sys.argv[1] , mode='r') as f:
		data = f.readlines()
	n = int(sys.argv[2])
	l = [(len(data)+i)//n for i in range(n)] #何個ずつに分けるかのリスト
	name = sys.argv[1].split('.')
	for i,num in enumerate(l):
		with open(name[0]+'-'+str(i)+'.'+name[1], mode='w') as fw:
			fw.write(''.join(data[:num]))
			data = data[num:]
