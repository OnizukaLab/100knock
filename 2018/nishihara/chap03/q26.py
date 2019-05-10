import re
import q20, q25

if __name__ == '__main__':
    string = q20.picktxt("../../../data/jawiki-country.json", "イギリス")
    basic = q25.basicinfo(string)
    print({k:re.sub("'''?|'{5}", "", v) for k,v in basic.items()})
