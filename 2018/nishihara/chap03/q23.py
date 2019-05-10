import re
import q20


if __name__ == '__main__':
    str = q20.picktxt("../../../data/jawiki-country.json", "イギリス")
    for line in str.split("\n"):
        if "=" in line[:1]:
            lv = len(min(re.findall("^=+|=+$", line)))
            print("{}: {}".format(line[lv:-lv].replace(" ", ""), lv))
