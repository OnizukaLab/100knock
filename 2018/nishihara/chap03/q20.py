import json

def picktxt(file, title):
    with open(file, "r") as f:
        for l in f.readlines():
            d = json.loads(l)
            if(d["title"] == title):
                return d["text"]


if __name__ == '__main__':
    print(picktxt("../../../data/jawiki-country.json", "イギリス"))
