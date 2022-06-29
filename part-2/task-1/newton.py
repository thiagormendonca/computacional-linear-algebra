import pandas as pd
import numpy as np


def func(x, teta):
    return np.array([
        2*x[1]**2 + x[0]**2 + 6*x[2]**2 - 1,
        8*x[1]**3 + 6*x[1]*x[0]**2 + 36*x[1]*x[0]
        * x[2] + 108*x[1]*x[2]**2 - teta[0],
        60*x[1]**4 + 60*x[1]**2*x[0]**2 + 576*x[1]**2*x[0] *
        x[2] + 2232*x[1]**2*x[2]**2 + 252*x[2]**2*x[0]**2
        + 1296*x[2]**3*x[0] + 3348*x[2]**4 + 24*x[0]**3*x[2] + 3*x[0] - teta[1]
    ])


def jacob(x):
    return pd.DataFrame([
        [2*x[0], 4*x[1], 12*x[2]],
        [12*x[1]*x[0] + 36*x[1]*x[2], 24*x[1] + 6*x[0]**2 + 36*x[0]*x[2] + 108*x[2]**2,
         36*x[1]*x[0] + 2*108*x[1]*x[2]],
        [120*x[1]**2*x[0] + 576*x[1]**2*x[2] + 2*252*x[2]**2*x[0] + 1296*x[2]**3 + 72*x[0]**2*x[2] + 3,
         240*x[1]**3 + 120*x[1]*x[0]**2 + 2*576 *
         x[1]*x[0]*x[2] + 2*2232*x[1]*x[2]**2,
         576*x[1]**2*x[0] + 2*2232*x[1]**2*x[2] + 2*252*x[2]*x[0]**2 + 3*1296*x[2]**2*x[0] + 4*3348*x[2]**3 + 24*x[0]**3]
    ])


def inverse(a):
    matrix = a.to_numpy()
    return np.linalg.inv(matrix)


def euclidian_norm(x):
    norm = 0

    for i in range(len(x)):
        norm += x[i] ** 2

    return norm ** (1/2)


def newton(x0, tol, niter, teta):
    k = 0
    x = x0

    while (k < niter):
        j = jacob(x)
        f = func(x, teta)

        dx = (-inverse(j)).dot(np.transpose(f))
        x = x + dx

        tolk = euclidian_norm(dx) / euclidian_norm(x)

        if (tolk < tol):
            return {'X': x, 'Iterações': k}

        k += 1

    return 'Número máximo de iterações atingido'
