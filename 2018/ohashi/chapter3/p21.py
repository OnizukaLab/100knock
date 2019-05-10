import json
import re
from p20 import get_britain

fp = open("jawiki-country.json", encoding='utf-8')

text = get_britain(fp)

fp.close()

for line in re.findall('(.+Category:.+)', text):
    print(line)






