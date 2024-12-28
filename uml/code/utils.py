import numpy as np

def generate_centering_matrix(n):
    I = np.eye(n)
    ones = np.ones((n, 1))
    H = I - (1/n) * (ones @ ones.T)
    return H
def get_gram(X):
    '''
    return -1/2 H X X^T H
    where X is the original distance matrix
    '''
    X2 = np.square(X)
    H = generate_centering_matrix(len(X))
    return -0.5 * H @ X @ H