
with open('hightemp.txt', mode='r') as fr, open('hightemp_11.txt', mode='w') as fw:
	fw.write(''.join([line.replace('\t',' ') for line in fr]))
