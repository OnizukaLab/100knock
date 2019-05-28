# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))
from q76 import generate_csv_style_data

data = generate_csv_style_data()
data = [row.split(",") for row in data.split("\n")]

data_length = len(data)
true_positive_count = 0
true_negative_count = 0
false_positive_count = 0
false_negative_count = 0

for row in data[:-1]:
    if row[0] == row[1] == "1":
        true_positive_count += 1
    elif row[0] == row[1] == "-1":
        true_negative_count += 1
    elif row[0] == "1" and row[1] != row[0]:
        false_positive_count += 1
    else:
        false_negative_count += 1

accuracy = (true_positive_count + true_negative_count) / data_length
precision = (true_positive_count) / (true_positive_count + false_positive_count)
recall = (true_positive_count) / (true_positive_count + false_negative_count)
f_measure = (2 * precision * recall) / (precision + recall)
print("accuracy: %0.4f" % (accuracy))
print("precision: %0.4f" % (precision))
print("recall: %0.4f" % (recall))
print("F-measure:%0.4f" % (f_measure))
