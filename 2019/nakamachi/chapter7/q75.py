# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))
from q72 import load_data, load_vectorizer
from q73 import load_model

lr = load_model()
y, X = load_data()
vectorizer = load_vectorizer()

coef = lr.coef_
coef = list(enumerate(list(coef[0])))

coef = sorted(coef, key=lambda item: item[1], reverse=True)
best_10 = list()
worst_10 = list()
for i in range(10):
    best_10.append(coef[i][0])
coef = sorted(coef, key=lambda item: item[1])
for i in range(10):
    worst_10.append(coef[i][0])

print("best 10")
print("-"*20)
for i in best_10:
    print(vectorizer.get_feature_names()[i])

print("")
print("worst 10")
print("-"*20)
for i in worst_10:
    print(vectorizer.get_feature_names()[i])
