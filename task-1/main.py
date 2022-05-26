import numpy as np
import pandas as pd

from lu_decomposition import lu_decomposition
from cholesky_decomposition import cholesky_decomposition
from jacobi import jacobi
from gauss_seidel import gauss_seidel


matrix_A = pd.read_csv('./mat_A.dat', sep=r'\s{2,}', engine='python', header=None)
vector_B = np.fromfile('./vet_B.dat', sep='\n')

icod = input('ICOD: ')
idet = input('IDET: ')
tolm = float(input('TOLm: '))

methods = {
    1: lu_decomposition(matrix_A, vector_B, idet),
    2: cholesky_decomposition(matrix_A, vector_B, idet),
    3: jacobi(matrix_A, vector_B, tolm),
    4: gauss_seidel(matrix_A, vector_B, tolm)
}

print(methods[icod])