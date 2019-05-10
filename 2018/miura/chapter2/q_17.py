
with open('hightemp.txt', mode='r') as f:
	print(set([line.split()[0] for line in f]))

