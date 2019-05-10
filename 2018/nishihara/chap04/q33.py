import q30

mor = q30.readma("../../../data/neko.txt.mecab")
for s in mor:
    for ma in s:
        if(ma["pos1"] == "サ変接続"):
            print(ma["base"])
