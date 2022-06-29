import pandas as pd
import numpy as np

from newton import func, inverse, euclidian_norm, jacob

def broyden_jacob(y, j, dx):
    y = np.array(y).reshape(len(y), 1)
    j = np.array(j)
    dx = np.array(dx).reshape(len(dx), 1)

    numerator = (y - (j).dot(dx)).dot(np.transpose(dx))
    denominator = np.transpose(dx).dot(dx)
    result = j + (numerator / denominator)

    return pd.DataFrame(result)


def broyden(x0, tol, niter, teta):
    k = 0
    x = x0
    b = jacob(x0)

    while (k < niter):
        j = b
        f = func(x, teta)

        dx = (-inverse(j)).dot(np.transpose(f))
        x = x + dx

        tolk = euclidian_norm(dx) / euclidian_norm(x)

        if (tolk <= tol):
            return {'X': x, 'Iterações': k}

        y = (func(x, teta) - f)
        b = broyden_jacob(y, j, dx)
        k += 1

    return 'Número máximo de iterações atingido'
