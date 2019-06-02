from scipy.sparse import csr_matrix
from q84 import WordContextMatrixGenerator
from utils import load_matrix, save_principal_vector, load_principal_vector, load_matrix_obj
from sklearn.decomposition import PCA, TruncatedSVD


def pca():
    print("Begin pca()")
    matrix = load_matrix_obj()
    print("loaded matrix")
    matrix = matrix.tocsr()
    print("done matrix modification")
    pca = TruncatedSVD(n_components=300)
    pca.fit_transform(matrix)
    print("done fit_transform")
    save_principal_vector(pca)

if __name__ == '__main__':
    pca()
