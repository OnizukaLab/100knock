import re
import q20


if __name__ == '__main__':
    str = q20.picktxt("../../../data/jawiki-country.json", "イギリス")
    for line in str.split("\n"):
        if "File:" in line or "ファイル:" in line:
            print(re.sub(".*(File|ファイル):([^|]+)\|.*", "\\2", line))
