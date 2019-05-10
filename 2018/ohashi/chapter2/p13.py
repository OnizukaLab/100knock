with open('merged.txt', 'w', encoding='utf-8') as f:
    with open('col1.txt', encoding='utf-8') as f2:
        with open('col2.txt', encoding='utf-8') as f3:
            for l1, l2 in zip(f2, f3):
                f.write(l1.replace('\n', '') + '\t' + l2)