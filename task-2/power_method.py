import numpy as np

def power_method(a, x0, lamb0, tol):
    y = np.array([0.] * len(x0))

    for i in range(len(a)):
        for j in range(len(a)):
            y[i] += a[j][i] * x0[j]

    lamb1 = y[0]
    y = y / lamb1

    r = abs(lamb1 - lamb0) / abs(lamb1)

    if (r <= tol):
        return (lamb1, y)

    return power_method(a, y, lamb1, tol)