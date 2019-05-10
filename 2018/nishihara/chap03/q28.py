import re
import q20, q25

if __name__ == '__main__':
    string = q20.picktxt("../../../data/jawiki-country.json", "イギリス")
    basic = q25.basicinfo(string)
    b = {k:re.sub("'''?|'{5}", "", v) for k,v in basic.items()}
    c = {k:re.sub("\[\[(ファイル:)?(.*?)((#.*?)?(\|.*?))?\]\]", "\\2", v) for k,v in b.items()}
    d = {k:re.sub("<ref.*?(/>|</ref>)|<br\s*/?>", "", v) for k,v in c.items()}

    for k,v in d.items():
        print("{}\t{}".format(k,v))
