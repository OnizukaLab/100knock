from q_20 import extract

print('\n'.join(line for line in extract('イギリス').split('\n') if 'ファイル' in line or 'File' in line))

'''
for line in extract('イギリス').split('\n'):
    if 'ファイル' in line:
        print(line)
'''
