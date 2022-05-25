import numpy as np
import pandas as pd

#Se A for uma matriz simétrica positiva definida é possível
def cholesky(a):
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

a = [[1,0.2,0.4],[0.2,1,0.5],[0.4,0.5,1]]
df = pd.DataFrame(np.array(a))
print(df)

cholesky(a)
df_cholesky = pd.DataFrame(np.array(a))
print(df_cholesky)


