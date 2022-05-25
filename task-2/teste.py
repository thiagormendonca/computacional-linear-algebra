import numpy as np

arr = np.array([[1.0,0.2,0.0],[0.2,1.0,0.5],[0.0,0.5,1.0]])

max = np.max(abs(arr))
result = np.where(abs(arr) == max)
print([result[0][0], result[1][0]])
print(result)

