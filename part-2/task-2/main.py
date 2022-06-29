import numpy as np
import pandas as pd

from bisection import bisection
from newton import newton

c = [0, 0, 0, 0]

icod = int(input('ICOD: '))
c[0] = float(input('C1: '))
c[1] = float(input('C2: '))
c[2] = float(input('C3: '))
c[3] = float(input('C4: '))
tolm = float(input('TOLm: '))


def root():
    method = int(
        input('1 - Bisseção\n2 - Newton\nDigite o número do método: '))

    a = 0
    b = 10

    methods = {
        1: lambda: bisection(a, b, tolm, c),
        2: lambda: newton((a+b)/2, 1000, tolm, c),
    }

    return methods[method]()


icods = {
    1: lambda: root(),
    2: lambda: None,
}

print(icods[icod]())
