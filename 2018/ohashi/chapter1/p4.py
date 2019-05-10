a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'.split()
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

print({(x[:1] if i+1 in index else x[:2]): i+1 for i,x in enumerate(a)})