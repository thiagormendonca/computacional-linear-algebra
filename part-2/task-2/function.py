from math import exp


def func(x, c):
    return c[0]*exp(c[1]*x) + c[2]*x**c[3]


def derivative(x, c):
    return c[1]*c[0]*exp(c[1]*x) + c[3]*c[2]*x**(c[3] - 1)
