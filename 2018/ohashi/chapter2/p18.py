with open('hightemp.txt', encoding='utf-8') as f:
    lines = [x for x in f]

def comp(x):
    return -float(x.split()[2])

lines.sort(key=comp)

for l in lines:
    print(l.replace('\n', ''))