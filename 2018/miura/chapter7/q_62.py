from q_61 import *

keys = [k.decode('utf-8') for k in r.keys()]
print(sum([1 for k in keys if get(k) == 'Japan']))
'''
count = 0
for k in keys:
	if get(k) == 'Japan':
		count += 1
print(count)
'''

