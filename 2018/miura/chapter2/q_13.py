
with open('col1.txt', mode='r') as f1, \
     open('col2.txt', mode='r') as f2, \
     open('hightemp_13.txt', mode='w') as fw:
	for line1,line2 in zip(f1,f2):
		fw.write(line1.strip() + '\t' + line2.strip() + '\n')

