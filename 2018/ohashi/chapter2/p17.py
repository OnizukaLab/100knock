with open('hightemp.txt', encoding='utf-8') as f:
    col1 = [x.split()[0] for x in f]

print(set(col1))