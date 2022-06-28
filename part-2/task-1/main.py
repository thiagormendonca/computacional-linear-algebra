import numpy as np
import pandas as pd
import sys

from newton import newton

teta = [0, 0]

icod = int(input('ICOD: '))
teta[0] = float(input('θ1: '))
teta[1] = float(input('θ2: '))
tolm = float(input('TOLm: '))

x0 = np.array([1., 0., 0.])

methods = {
    1: lambda: newton(x0, tolm, 1000, np.array(teta)),
    2: lambda: None,
}

print(methods[icod]())
