import q30

mor = q30.readma("../../../data/neko.txt.mecab")
for s in mor:
    for m in zip(s, s[1:], s[2:]):
        if(m[0]["pos"] == "名詞" and m[1]["surface"] == "の" and m[2]["pos"] == "名詞"):
            rst = "".join([w["surface"] for w in m])
            print(rst)
