import numpy as np

def iteration(a, x0, lamb0, tol, it = 0):
    y = np.array([0.] * len(x0))

    for i in range(len(a)):
        for j in range(len(a)):
            y[i] += a[j][i] * x0[j]

    lamb1 = find_greatest(y)
    y = y / lamb1

    r = abs(lamb1 - lamb0) / abs(lamb1)

    if (r <= tol):
        return lamb1, y, it

    return iteration(a, y, lamb1, tol, it + 1)

def find_greatest(a):
    greatest = float('-inf')

    for i in range(len(a)):
        if (a[i] > greatest):
            greatest = a[i]

    return greatest

def power_method(a, tol):
    x0 = np.array([1] * len(a))

    lamb, x, it = iteration(a, x0, 1, tol)

    return { 'Autovalor': lamb, 'Autovetor': x, 'Número de iterações': it }

