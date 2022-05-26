import numpy as np
import math

def input_functions():
    finish = False
    functions = []

    print('Select functions to apply in x based on python "math" module')
    print('For help: https://docs.python.org/3/library/math.html \n')

    while not finish:
        function = input('Input a function: ')

        if hasattr(math, function):
            is_parameter = input('Is there any other parameter for the function? Y / N')
            if is_parameter == 'Y':
                parameter = input('Select a parameter: \n')
                function = [function, int(parameter)]
            functions.append(function)
        else:
            print('This is not a valid function')
            print('For help: https://docs.python.org/3/library/math.html \n')

        is_finish = input('Do you finish? Y / N \n')
        if is_finish == 'Y':
            finish = True

    return functions


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

def multilinear_regression(x_coords, y_coords, x):
    functions = input_functions()
    b = generate_coefficients(x_coords, y_coords, functions)

    estimated_y = 0
    for k in range(len(functions)):
        estimated_y += b[k] * apply_func(x, functions[k])

    return { 'Valor estimado': estimated_y }











