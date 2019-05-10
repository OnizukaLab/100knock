from q_20 import extract
import re

basic_dict = {}
for line in extract('イギリス').split('\n'):
    if re.match('^\|.* = .*', line):
        s = re.sub(r'<.*>', '', line.replace('|','').replace('[[','').replace(']]','').replace('{{','').replace('}}','').replace("'",''))
        word = re.split(' = ', s)
        basic_dict[word[0]] = word[1]

if __name__ == '__main__':
    for k,v in basic_dict.items():
        print(k + ' : ' + v)
