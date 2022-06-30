from math import cos, sin


def F(t, a, w):
    return a[0]*sin(w[0]*t) + a[1]*sin(w[1]*t) + a[2]*cos(w[2]*t)


def f(t, x, xl, a, w, k, c, m):
    return (F(t, a, w) - k*x - c*xl)/m


def rkn(h, total, a, w, k, c, m):
    n = int(total/h)
    t = 0
    x = 0
    xl = 0

    t_list = []
    x_list = []
    xl_list = []
    xll_list = []

    for i in range(n):
        t = i * h

        xll = f(t, x, xl, a, w, k, c, m)

        t_list.append(t)
        x_list.append(x)
        xl_list.append(xl)
        xll_list.append(xll)

        k1 = 1/2*h * f(t, x, xl, a, w, k, c, m)
        q = 1/2*h * (xl + 1/2*k1)
        k2 = 1/2*h * f(t + h/2, x + q, xl + k1, a, w, k, c, m)
        k3 = 1/2*h * f(t + h/2, x + q, xl + k2, a, w, k, c, m)
        l = h * (xl + k3)
        k4 = 1/2*h * f(t + h, x + l, xl + 2*k3, a, w, k, c, m)

        x = x + h * (xl + 1/3 * (k1 + k2 + k3))
        xl = xl + 1/3*(k1 + 2*k2 + 2*k3 + k4)

    t_list.append(t)
    x_list.append(x)
    xl_list.append(xl)
    xll_list.append(xll)

    return t_list, x_list, xl_list, xll_list
