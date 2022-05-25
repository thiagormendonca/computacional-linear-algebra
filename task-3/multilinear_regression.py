import numpy as np
import math

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
            x = apply_func(x_coords[i], functions[j])
            row.append(x)
        p.append(row)

    return p

def generate_coefficients(x_coords, y_coords, functions):
    p = np.asarray(generate_p(x_coords, functions))
    p_t = np.matrix.transpose(p)

    b = np.linalg.inv(np.dot(p_t, p)).dot(p_t).dot(y_coords)

    return b

def multilinear_regression(x_coords, y_coords, functions, x):
    b = generate_coefficients(x_coords, y_coords, functions)

    estimated_y = 0
    for k in range(len(functions)):
        estimated_y += b[k] * apply_func(x, functions[k])

    return estimated_y

print(multilinear_regression([1,2,3],[2,3.5,6.5],[["pow", 0],["pow", 1]], 7))
#print(multilinear_regression([1,4,25],[],["sin","cos","sqrt", ["pow", 2]]))








