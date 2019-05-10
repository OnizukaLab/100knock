from q_20 import extract
import re

for line in extract('イギリス').split('\n'):
	m = re.match('^(==+).*?(==+)$', line)
	if m:
		print(line)
		f = len(m.group(1))
		l = len(m.group(2))
		#print(line.strip('='), max(len(m.group(1)),len(m.group(2))))
		print(f,l)
		print(line.strip('='), max(f,l))
