import pandas as pd
import sys

from lagrange import lagrange
from multilinear_regression import multilinear_regression

X_Y = pd.read_csv('./task-3/pointsa.dat', sep=r'\s{2,}', engine='python', header=None)

icod = int(input('ICOD: '))
x = float(input('x: '))

methods = {
    1: lambda: lagrange(X_Y[0], X_Y[1], x),
    2: lambda: multilinear_regression(X_Y[0], X_Y[1], x),
}

with open('./task-3/output.txt', 'w') as f:
    sys.stdout = f
    print(methods[icod]())