s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one = [1,5,6,7,8,9,15,16,19]
element_dict = {}
for i,word in enumerate(s.split(" ")):
	n = 1 if (i+1) in one else 2
	element_dict[word[:n]] = (i+1)
print(element_dict)
