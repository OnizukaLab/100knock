from q_20 import extract

'''
for line in extract('イギリス').split('\n'):
	if 'Category:' in line:
		print(line.strip('[]|*').replace('Category:',''))
'''

print('\n'.join([line.strip('[]|*').replace('Category:','') for line in extract('イギリス').split('\n') if 'Category:' in line]))
