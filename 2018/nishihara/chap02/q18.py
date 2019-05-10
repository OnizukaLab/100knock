with open("hightemp.txt", "r") as file:
    l = list(file)
    l.sort(key=lambda x: -float(x.split()[2]))
    print("".join(l))
