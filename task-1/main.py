import numpy as np
import pandas as pd
from jacobi import jacobi

from lu_decomposition import lu_decomposition


matrix_A = pd.read_csv('./mat_A.dat', sep=r'\s{2,}', engine='python', header=None)
vector_B = np.fromfile('./vet_B.dat', sep='\n')

icod = input('ICOD: ')
idet = input('IDET: ')
tolm = float(input('TOLm: '))

methods = {
    1: lu_decomposition(matrix_A, vector_B, idet),
    3: jacobi(matrix_A, vector_B, tolm)
}

print(methods[icod])