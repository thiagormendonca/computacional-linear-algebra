from function import func, derivative


def newton(x0, niter, tol, c):
    x = x0

    for k in range(niter):
        xk = x - func(x, c)/derivative(x, c)
        tolk = abs(xk - x)

        if (tolk < tol):
            return {'X': xk, 'Iterações': k}

        x = xk

    return 'Número máximo de iterações atingido'
