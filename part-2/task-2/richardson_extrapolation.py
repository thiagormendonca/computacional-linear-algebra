import math

from finite_differences import forward

def richardson_extrapolation(x, c, dx1, dx2):
    # Assuming linear term as dominant
    p = 1
    q = dx1 / dx2

    d_values = []
    for dx in [dx1, dx2]:
        d = forward(x, c, dx)
        d_values.append(d)

    [d1, d2] = d_values
    derivative = d1 + ((d1 - d2) / (math.pow(q, -p) - p))

    return derivative


