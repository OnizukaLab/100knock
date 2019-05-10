s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(word) for word in s.replace(',','').replace('.','').split(" ")])

'''
#等価
result = []
for word in s.replace(',','').replace('.','').split(' '):
	result.append(len(word))
print(result)
'''
