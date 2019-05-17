import sys
from os import path

sys.path.append(path.abspath(path.curdir))
from data_loader import data_loader

data = data_loader()
positive_count = 0
negative_count = 0

for line in data:
    if line.find("+1") == 0:
        positive_count += 1
    else:
        negative_count += 1

print("positive count: %d" % positive_count)
print("negative count: %d" % negative_count)