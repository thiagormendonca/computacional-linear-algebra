import numpy as np
import pandas as pd

from power_method import power_method
from jacobi_method import jacobi_method

matrix_A = pd.read_csv('./task-2/mat_A.dat', sep=r'\s{2,}', engine='python', header=None)

icod = int(input('ICOD: '))
idet = int(input('IDET: '))
tolm = float(input('TOLm: '))

methods = {
    1: lambda: power_method(matrix_A, tolm),
    2: lambda: jacobi_method(matrix_A, tolm),
}

print(methods[icod]())