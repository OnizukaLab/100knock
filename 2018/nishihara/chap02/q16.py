import sys

with open("hightemp.txt", "r") as file:
    l = file.readlines()
    n = int(len(l) / int(sys.argv[1]))
    for j,i in enumerate(range(0,len(l),n)):
        with open("hightemp-" + str(j) + ".txt", "w") as out:
            out.write("".join(l[i:i + n]))
