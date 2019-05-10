
with open('hightemp.txt', mode='r') as f:
	data = f.readlines()
	print(''.join(sorted(data, key=lambda x:float(x.split()[2]), reverse=True)), end='')

	'''
	data = [line.strip() for line in f]
	sorted_data = sorted(data, key=lambda x:float(x.split()[2]), reverse=True)
	for line in sorted_data:
		print(line)
	'''
