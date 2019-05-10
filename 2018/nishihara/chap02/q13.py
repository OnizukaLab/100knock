file = open("col1col2.txt", "w")
col1 = open("col1.txt", "r")
col2 = open("col2.txt", "r")

# c1 = col1.readlines()
c2 = col2.readlines()

# for i in range(len(c1)):
#     print(c1[i].strip() + "\t" + c2[i].strip() + "\n")

for i,c1 in enumerate(col1):
    file.write(c1.strip() + "\t" + c2[i].strip() + "\n")

col1.close()
col2.close()
file.close()