
with open('hightemp.txt', mode='r') as fr, \
     open('col1.txt', mode='w') as fw1, \
     open('col2.txt', mode='w') as fw2:
	for line in fr:
		row = line.strip().split('\t')
		fw1.write(row[0]+'\n')
		fw2.write(row[1]+'\n')
	
