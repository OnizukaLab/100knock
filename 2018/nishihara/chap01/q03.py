import re

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi = []
for s in re.sub(r"[,.]", "", string).split(" "):
    pi.append(len(s))
print(pi)
