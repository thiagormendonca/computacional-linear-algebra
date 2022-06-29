import numpy as np
import pandas as pd

from newton import newton
from broyden import broyden

teta = [0, 0]

icod = int(input('ICOD: '))
teta[0] = float(input('θ1: '))
teta[1] = float(input('θ2: '))
tolm = float(input('TOLm: '))

x0 = np.array([1., 0., 0.])

methods = {
    1: lambda: newton(x0, tolm, 1000, np.array(teta)),
    2: lambda: broyden(x0, tolm, 1000, np.array(teta)),
}

with open('./task-1/output.txt', 'w') as f:
    sys.stdout = f
    print(methods[icod]())

