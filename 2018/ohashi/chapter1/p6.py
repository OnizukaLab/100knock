from p5 import n_gram

a = [x for x in 'paraparaparadise']
b = [x for x in 'paragraph']

X = set(n_gram(a, 2))
Y = set(n_gram(b, 2))

print(X | Y)
print(X & Y)
print(X - Y)
