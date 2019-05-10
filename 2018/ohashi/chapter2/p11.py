with open('hightemp.txt', encoding='utf-8') as f:
    for line in f:
        print(line.replace('\t', ' '))