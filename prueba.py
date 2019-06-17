import numpy as np
print("hola mundo")
print("Holiis")

from matplotlib import pyplot as plt

A = [1,2,3]
B = [4,5,6]
C = [7, 8, 9]

A = np.array(A)
B = np.array(C)

plt.figure()
plt.scatter(A,B)
plt.show()
