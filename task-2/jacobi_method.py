import numpy as np
import pandas as pd
import sys


def iteration(a, x, tol, it = 0):
    p = generate_p(a)
    a = np.dot(np.matrix.transpose(p), a).dot(p)
    x = np.dot(x, p)

    i, j = get_max_indexes(a)
    r = abs(a[j][i])

    if (r <= tol):
        return np.array(np.diagonal(a)), pd.DataFrame(x), it

    return iteration(a, x, tol, it + 1)

def generate_p(a):
    # Get max indexes
    i, j = get_max_indexes(a)

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
    indexes = (0, 1)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j: continue
            if abs(a[i][j]) > abs(a[indexes[0]][indexes[1]]):
                indexes = (i, j)
    return indexes

def theta(a, i, j):
    if a[i][i] != a[j][j]:
        return (np.arctan((2 * a[j][i]) / (a[i][i] - a[j][j]))) / 2
    else:
        return np.pi / 4

def det(a):
    p = 1
    for eigenvalue in a:
        p *= eigenvalue

    return p

def is_symmetric(a):
    a_t = np.transpose(a)
    return np.array_equal(a, a_t)

def jacobi_method(a, tol, idet):
    if not (is_symmetric(pd.DataFrame.to_numpy(a))):
        return { 'Error': 'matrix is not symmetric' }

    x0 = np.identity(len(a))
    matrix_det = None

    lamb, x, it = iteration(pd.DataFrame.to_numpy(a), x0, tol)

    if (idet > 0):
        matrix_det = det(lamb)

    return {'Autovalor': lamb, 'Autovetor': x, 'Número de iterações': it, 'Determinante': matrix_det}

