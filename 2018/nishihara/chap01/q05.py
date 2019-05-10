def ngram(tlist, n):
    l = []
    for i in range(len(tlist) - n + 1):
        l.append(tlist[i:i+n])
    return l


str = "I am an NLPer"
print(ngram(str.split(" "), 2))
print(ngram(str, 2))