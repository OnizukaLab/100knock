import sys
from os import path

import numpy as np

sys.path.append(path.abspath(path.curdir))
from q72 import load_data
from q73 import load_model

lr = load_model()
y, X = load_data()

print(lr.predict(X))


