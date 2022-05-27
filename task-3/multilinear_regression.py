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










