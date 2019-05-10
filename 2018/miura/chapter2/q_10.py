
count = 0
with open('hightemp.txt', mode='r') as f:
	print(len(f.readlines()))

'''
with open('hightemp.txt', mode='r') as f:
	print(sum([1 for line in f]))
'''

