def gauss_seidel(a, b, x0, tol):
    x1 =x0.copy()

    for i in range(len(a)):
        sum = 0
        for j in range(i):
            sum += a[i][j] * x1[j]
        for j in range(i + 1, len(a)):
            sum += a[i][j] * x0[j]
        x1[i] = (b[i] - sum) / a[i][i]

    r = euclidian_norm(dif(x0, x1)) / euclidian_norm(x1)

    if (r <= tol):
        return x1

    return gauss_seidel(a, b, x1, tol)

def dif(x0, x1):
    x = []
    for i in range(len(x0)):
        x.append(x1[i] - x0[i])
    return x

def euclidian_norm(x):
    norm = 0

    for i in range(len(x)):
        norm += x[i] ** 2

    return norm ** (1/2)

a = [[3,-1,-1],[-1,3,-1],[-1,-1,3]]
b = [1,2,1]
x0 = [1.000,1.000,1.000]
tol = 0.001
print(gauss_seidel(a, b, x0, tol))