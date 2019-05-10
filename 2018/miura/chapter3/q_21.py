from q_20 import extract

'''
for line in extract('イギリス').split('\n'):
	if 'Category:' in line:
		print(line)
'''

print('\n'.join([line for line in extract('イギリス').split('\n') if 'Category:' in line]))

