string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]

print(dict(map(lambda x: (x[1][:1 if x[0]+1 in nums else 2], x[0]), enumerate(string.replace(".", "").split(" ")))))
