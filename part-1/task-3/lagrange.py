import numpy as np


def lagrange(x, y, coord):
    phi = np.array([1.] * len(y))

    for i in range(len(y)):
        for k in range(len(x)):
            if (k == i): continue
            phi[i] = phi[i] * ((coord - x[k])/(x[i] - x[k]))

    result = 0

    for i in range(len(phi)):
        result += phi[i] * y[i]

    return { 'Valor estimado': result }