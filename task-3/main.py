import pandas as pd

from lagrange import lagrange
from multilinear_regression import multilinear_regression

vector_X = pd.read_csv('./task-2/vector_X.dat', sep=r'\s{2,}', engine='python', header=None)
vector_Y = pd.read_csv('./task-2/vector_Y.dat', sep=r'\s{2,}', engine='python', header=None)

icod = int(input('ICOD: '))
x = float(input('x: '))

methods = {
    1: lambda: lagrange(vector_X, vector_Y, x),
    2: lambda: multilinear_regression(vector_X, vector_Y, x),
}

print(methods[icod]())