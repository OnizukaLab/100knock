import sys

with open("hightemp.txt", "r") as file:
    print("".join(file.readlines()[:int(sys.argv[1])]).rstrip())
