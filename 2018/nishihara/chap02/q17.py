with open("hightemp.txt", "r") as file:
    print(set([row.split()[0] for row in file]))
