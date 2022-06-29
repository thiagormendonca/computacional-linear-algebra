from function import func


def bisection(a, b, tol, c):
    k = 0

    while abs(b - a) > tol:
        x = (a + b) / 2.0
        f = func(x, c)

        if (f > 0):
            b = x
        else:
            a = x

        k += 1

    return {'X': x, 'Iterações': k}
