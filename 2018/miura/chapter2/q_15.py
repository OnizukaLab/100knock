import sys
if len(sys.argv) < 3:
	print('usage: python q_15.py <filename> <number>')
else:
	with open(sys.argv[1], mode='r') as f:
		print(''.join(f.readlines()[-int(sys.argv[2]):]),end='')
