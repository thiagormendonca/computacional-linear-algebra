import numpy as np
import pandas as pd

def generate_p(a):
    # Get max indexes
    indexes = get_max_indexes(a)
    i = indexes[0]
    j = indexes[1]

    # Define theta
    th = theta(a, i, j)

    # Generate P
    p = np.identity(len(a))
    p[i][i] = np.cos(th)
    p[j][j] = np.cos(th)
    p[i][j] = - np.sin(th)
    p[j][i] = np.sin(th)
    return p

def get_max_indexes(a):
    indexes = [0, 1]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j: continue
            if abs(a[i][j]) > abs(a[indexes[0]][indexes[1]]):
                indexes = [i, j]
    return indexes

def theta(a, i, j):
    if a[i][i] != a[j][j]:
        return (np.arctan((2 * a[i][j]) / (a[i][i] - a[j][j]))) / 2
    else:
        return np.pi / 4


def jacobi_method(a, tol, x=None):
    if x is None: x = np.identity(len(a))

    p = generate_p(a)
    a = np.dot(np.matrix.transpose(p), a).dot(p)
    x = np.dot(x, p)

    indexes = get_max_indexes(a)
    r = a[indexes[0]][indexes[1]]

    if (r <= tol):
        return np.diagonal(a), x

    return jacobi_method(a, tol, x)

a = [[1.0,0.2,0.0],[0.2,1.0,0.5],[0.0,0.5,1.0]]
print(pd.DataFrame(jacobi_method(a, 0.01))[0])