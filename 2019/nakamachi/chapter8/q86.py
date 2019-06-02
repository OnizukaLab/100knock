from q84 import Count
from q85 import WordContextMatrixGenerator
from utils import load_principal_vector, load_matrix, save_matrix_obj, save_term_list, load_matrix_obj, load_term_list
import numpy as np

# matrix = load_matrix()
pca = load_principal_vector()

term_list = load_term_list()

def fixer():
    # matrix = load_matrix_obj()
    # matrix = matrix.tocsr()
    # save_matrix_obj(matrix)
    matrix = load_matrix()
    save_matrix_obj(matrix.matrix.tocsr())
    save_term_list(matrix.term_list)

def generate_vector(word):
    index = 0
    try:
        index = term_list.index(word)
        vector = pca.components_[:, index]
        return vector.reshape((1, len(vector)))
    except:
        pass

if __name__ == '__main__':
    #fixer()
    US = generate_vector("United_States")
    print(US)
