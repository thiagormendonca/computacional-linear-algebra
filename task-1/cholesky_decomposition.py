import numpy as np
import pandas as pd

from lu_decomposition import y, x, det

def decomposition(a):
    for i in range(len(a)):
        sum = 0
        for k in range(i):
            sum += (a[i][k]) ** 2
        a[i][i] = (a[i][i] - sum) ** 0.5

        sum = 0
        step = 1
        for j in range(i + 1, len(a), step):
            if (j != i + 1): step += 1
            for k in range(i):
                sum += a[i][k] * a[j][k]
            a[j][i] = (a[i][j] - sum) / a[i][i]

    return a

# Checar se A for uma matriz simétrica positiva definida é possível
def cholesky_decomposition(a, b, idet):
    lu = decomposition(a)

    y_vec = y(lu, b)
    x_vec = x(np.transpose(lu), y_vec)

    if (idet > 0):
        matrix_det = det(lu)

    return {'Resultado': x_vec, 'Determinante': matrix_det}


a = [[1,0.2,0.4],[0.2,1,0.5],[0.4,0.5,1]]
b = [[0.6, -0.3, -0.6]]

cholesky_decomposition(pd.DataFrame(a), np.array(b), 1)
df_cholesky = pd.DataFrame(a)
print(df_cholesky)




