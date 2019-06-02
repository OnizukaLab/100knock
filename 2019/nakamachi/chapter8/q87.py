from q84 import Count
from q85 import WordContextMatrixGenerator
from q86 import generate_vector
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_principal_vector, load_matrix
import numpy as np


if __name__ == '__main__':
    United_States = generate_vector("United_States")
    US = generate_vector("US")

    print(cosine_similarity(United_States, US))