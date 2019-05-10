import re
a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'.split()

print(list(map(lambda x: len(re.sub('\.|,', '', x)), a)))