col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

with open("hightemp.txt", "r") as file:
    for row in file:
        col1.write(row.split()[0] + "\n")
        col2.write(row.split()[1] + "\n")

col1.close()
col2.close()
