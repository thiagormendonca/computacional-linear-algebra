from matplotlib import pyplot as plt
import numpy as np

from rkn import rkn

h = float(input('Passo: '))
total = int(input('Tempo total: '))

m = 1
c = 0.1
k = 2

a = np.array([1., 2., 1.5])
w = np.array([0.05, 1., 2.])

t, x, xl, xll = rkn(h, total, a, w, k, c, m)

plt.plot(t, x, label='Deslocamento')
plt.plot(t, xl, label='Velocidade')
plt.plot(t, xll, label='Aceleração')

plt.xlabel('tempo')

plt.legend()

plt.savefig('./graph.png')
