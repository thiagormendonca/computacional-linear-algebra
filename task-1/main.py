import numpy as np
import pandas as pd

from lu_decomposition import lu_decomposition
from cholesky_decomposition import cholesky_decomposition
from jacobi import jacobi
from gauss_seidel import gauss_seidel


matrix_A = pd.read_csv('./task-1/mat_A.dat', sep=r'\s{2,}', engine='python', header=None)
vector_B = np.fromfile('./task-1/vet_B.dat', sep='\n')

icod = int(input('ICOD: '))
idet = int(input('IDET: '))
tolm = float(input('TOLm: '))

methods = {
    1: lambda: lu_decomposition(matrix_A, vector_B, idet),
    2: lambda: cholesky_decomposition(matrix_A, vector_B, idet),
    3: lambda: jacobi(matrix_A, vector_B, tolm),
    4: lambda: gauss_seidel(matrix_A, vector_B, tolm)
}

print(methods[icod]())