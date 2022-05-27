import numpy as np
import math
import sys
import pandas as pd


def apply_func(x, function):
    if type(function) is list:
        result = getattr(math, function[0])(x, function[1])
    else:
        result = getattr(math, function)(x)

    return result

def generate_p(x_coords, functions):
    p = []
    for i in range(len(x_coords)):
        row = []
        for j in range(len(functions)):
            x = x_coords[i]
            for func in functions[j]:
                x = apply_func(x, func)
            row.append(x)
        p.append(row)
    return p

def generate_coefficients(x_coords, y_coords, functions):
    p = np.asarray(generate_p(x_coords, functions))
    p_t = np.matrix.transpose(p)

    b = np.linalg.inv(np.dot(p_t, p)).dot(p_t).dot(y_coords)

    return b

def multilinear_regression(x_coords, y_coords, x):
    functions = [[["pow", 0]], [["pow", -1], "exp"], [["pow", -2]]]
    #functions = [[["pow", 0]], [["pow", 1]]]
    #functions = [["exp", ["pow", -1]], ["log"]]
    b = generate_coefficients(x_coords, y_coords, functions)

    estimated_y = 0
    for k in range(len(functions)):
        omega = x
        for func in functions[k]:
            omega = apply_func(omega, func)
        estimated_y += b[k] * omega

    return { 'Valor estimado': estimated_y }

#print(multilinear_regression(np.array([1.0,2.0,3.0]), np.array([2.0,3.5,6.5]), 5))
#print(multilinear_regression(np.array([1.0,2.0,4.0]), np.array([1.05,3.22,6.02]), 5))


X_Y = pd.read_csv('./pointsa.dat', sep=r'\s{2,}', engine='python', header=None)
result = multilinear_regression(X_Y[0], X_Y[1], 5.5)

with open('./output.txt', 'w') as f:
    sys.stdout = f
    print(result)









