import numpy as np

def iteration(a, b, x0, tol, it=0):
    x1 = x0.copy()

    for i in range(len(a)):
        sum = 0
        for j in range(i):
            sum += a[j][i] * x1[j]
        for j in range(i + 1, len(a)):
            sum += a[j][i] * x0[j]
        x1[i] = (b[i] - sum) / a[i][i]

    r = euclidian_norm(x1 - x0) / euclidian_norm(x1)

    if (r <= tol):
        return x1, it

    return iteration(a, b, x1, tol, it + 1)

def euclidian_norm(x):
    norm = 0

    for i in range(len(x)):
        norm += x[i] ** 2

    return norm ** (1/2)

def gauss_seidel(a, b, tol):
    x0 = np.array([1.] * len(b))

    result, it = iteration(a, b, x0, tol)

    return { 'Resultado': result, 'Número de iterações': it }

