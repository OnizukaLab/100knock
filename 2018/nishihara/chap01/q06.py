def ngram(tlist, n):
    l = []
    for i in range(len(tlist) - n + 1):
        l.append(tlist[i:i+n])
    return l


X = set(ngram("paraparaparadise", 2))
Y = set(ngram("paragraph", 2))

print(X | Y)
print(X & Y)
print(X - Y)
print('se' in X)
print('se' in Y)
