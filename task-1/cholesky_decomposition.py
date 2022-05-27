import numpy as np
import pandas as pd
import sys
from lu_decomposition import det

def decomposition(a):
    for i in range(len(a)):
        sum = 0
        for k in range(i):
            sum += (a[k][i]) ** 2
        a[i][i] = (a[i][i] - sum) ** 0.5

        sum = 0
        step = 1
        for j in range(i + 1, len(a), step):
            if (j != i + 1): step += 1
            for k in range(i):
                sum += a[k][i] * a[k][j]
            a[i][j] = (a[j][i] - sum) / a[i][i]
            if not float((a[j][i] - sum) / a[i][i]):
                print((a[j][i] - sum) / a[i][i])

    return a

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

def forward_sub(l, b):
    for i in range(len(l)):
        sum = 0
        for j in range(i):
            sum += l[i][j] * b[j]
        b[i] = (b[i] - sum) / l[i][i]

    return b

def forward_sub(l, b):
    for i in range(len(l)):
        sum = 0
        for j in range(i):
            sum += l[i][j] * b[j]
        b[i] = (b[i] - sum) / l[i][i]

    return b

def retro_sub(u, y):
    for i in range(len(u) - 1, -1, -1):
        sum = 0
        for j in range(i + 1, len(u)):
            sum += u[i][j] * y[j]
        y[i] = (y[i] - sum) / u[i][i]

    return y

def cholesky_decomposition(a, b, idet):
    if not (is_pos_def(pd.DataFrame.to_numpy(a))):
        return { 'Error': 'Matrix is not positive definite' }

    lu = decomposition(a)

    y_vec = forward_sub(np.tril(pd.DataFrame.to_numpy(lu)), b)
    x_vec = retro_sub((np.transpose(np.tril(pd.DataFrame.to_numpy(lu)))), y_vec)

    if (idet > 0):
        matrix_det = det(lu)

    return {'Resultado': np.array(x_vec), 'Determinante': matrix_det}

matrix_A = pd.read_csv('./mat_A.dat', sep=r'\s{2,}', engine='python', header=None)
vector_B = np.fromfile('./vet_B.dat', sep='\n')

with open('./output.txt', 'w') as f:
    sys.stdout = f
    print(cholesky_decomposition(matrix_A, vector_B, 1))




