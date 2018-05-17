import re
import q20


if __name__ == '__main__':
    string = q20.picktxt("../../../data/jawiki-country.json", "イギリス")
    s = re.search("{{[^}]*基礎情報[^{}]*({{[^{}]*}}[^{}]*)*}}",\
        string, flags=re.DOTALL).group()
    print(dict([tuple(re.split(" *= *", l[1:], 1)) for l in s.split("\n") if "=" in l]))
