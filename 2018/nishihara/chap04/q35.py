import q30

mor = q30.readma("../../../data/neko.txt.mecab")
rst = []

for s in mor:
    for m in s:
        if(m["pos"] == "名詞"):
            rst.append(m["surface"])
        else:
            if(len(rst) > 1):
                print("".join(rst))
            rst = []
