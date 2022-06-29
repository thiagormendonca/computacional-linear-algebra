import numpy as np
import pandas as pd

from bisection import bisection
from newton import newton
from polynomial_quadrature import polynomial_quadrature
from gaussian_quadrature import gaussian_quadrature
from finite_differences import forward, backward, central
from richardson_extrapolation import richardson_extrapolation

c = [0, 0, 0, 0]

icod = int(input('ICOD: '))
c[0] = float(input('C1: '))
c[1] = float(input('C2: '))
c[2] = float(input('C3: '))
c[3] = float(input('C4: '))


def root():
    method = int(
        input('1 - Bisseção\n2 - Newton\nDigite o número do método: '))

    a = float(input('a: '))
    b = float(input('b: '))
    tolm = float(input('TOLm: '))

    methods = {
        1: lambda: bisection(a, b, tolm, c),
        2: lambda: newton((a+b)/2, 1000, tolm, c),
    }

    return methods[method]()


def integral():
    method = int(
        input('1 - Quadratura Polinomial\n2 - Quadratura de Gauss\nDigite o número do método: '))

    a = 1
    b = 2
    numP = 6

    methods = {
        1: lambda: polynomial_quadrature(a, b, numP, c),
        2: lambda: gaussian_quadrature(a, b, numP, c),
    }

    return methods[method]()


def finite_differences():
    method = int(
        input('1 - Passo a frente\n2 - Passo atrás\n3 - Central\nDigite o número do método: '))

    x = float(input('x: '))
    dx = float(input('dx: '))

    methods = {
        1: lambda: forward(x, c, dx),
        2: lambda: backward(x, c, dx),
        3: lambda: central(x, c, dx)
    }

    return methods[method]()


def derivative_re():
    dx1 = float(input('dx1: '))
    dx2 = float(input('dx2: '))
    x = float(input('x: '))

    return richardson_extrapolation(x, c, dx1, dx2)

icods = {
    1: lambda: root(),
    2: lambda: integral(),
    3: lambda: finite_differences(),
    4: lambda: derivative_re()
}

with open('./output.txt', 'w') as f:
    sys.stdout = f
    print(methods[icod]())
