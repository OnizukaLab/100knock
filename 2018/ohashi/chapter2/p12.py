with open('hightemp.txt', encoding='utf-8') as f:
    with open('col1.txt', 'w', encoding='utf-8') as f2:
        with open('col2.txt', 'w', encoding='utf-8') as f3:
            for line in f:
                tmp = line.split()
                f2.write(tmp[0] + '\n')
                f3.write(tmp[1] + '\n')



