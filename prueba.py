import numpy as np
print("hola mundo")

from matplotlib import pyplot as plt

A = [1,2,3]
B = [4,5,6]

A = np.array(A)
B = np.array(B)

plt.figure()
plt.scatter(A,B)
plt.show()
