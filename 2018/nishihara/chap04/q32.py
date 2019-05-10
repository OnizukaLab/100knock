import q30

mor = q30.readma("../../../data/neko.txt.mecab")
for s in mor:
    for ma in s:
        if(ma["pos"] == "動詞"):
            print(ma["base"])
