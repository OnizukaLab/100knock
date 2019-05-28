# need to set chapter7 as resource root.
# import sys
# from os import path
# sys.path.append(path.abspath(path.curdir))

from q72 import load_data
from q73 import load_model

lr = load_model()
y, X = load_data()

print(lr.predict(X))
