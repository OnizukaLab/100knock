import collections

with open('hightemp.txt', mode='r') as f:
	counter = collections.Counter([line.split()[0] for line in f])
	for c in counter.most_common():
		print(c)
