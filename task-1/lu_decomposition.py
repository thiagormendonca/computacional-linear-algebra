def decomposition(a):
    for k in range(len(a)):
        for i in range(k + 1, len(a)):
            a[k][i] = a[k][i]/a[k][k]
        
        for j in range(k + 1, len(a)):
            for i in range(k + 1, len(a)):
                a[j][i] = a[j][i] - (a[k][i] * a[j][k])

    return a

def y(l, b):
    # percorre todas as linhas de l
    for i in range(len(b)):
        # para cada linha de b, percorre suas colunas antes da diagonal
        for j in range(i):
            # para cada elemento, subtrai da multiplicação da inversa por b
            b[i] += -l[j][i] * b[j]

    return b

def x(u, y):
    # percorre inversamente todas as linhas de u
    for i in range(len(y) - 1, -1, -1):
        # para cada linha de u, percorre inversamente suas colunas depois da diagonal
        for j in range(len(u) - 1, i, -1):
            # para cada elemento, subtrai da multiplicação dos Xs já calculados
            y[i] -= (u[j][i] * y[j])
        # para o elemento da diagonal, divide o resultado pelo coeficiente
        y[i] = y[i] / u[i][i]

    return y

def lu_decomposition(a, b, idet):
    lu = decomposition(a)
    matrix_det = None

    if (idet > 0):
        matrix_det = det(lu)

    y_vec = y(lu, b)
    x_vec = x(lu, y_vec)

    return { 'Resultado': x_vec, 'Determinante': matrix_det }

def det(a):
    result = 1

    for i in range(len(a)):
        result = result * a[i][i]

    return result