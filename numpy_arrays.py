import numpy as np
from numpy.ma.core import identity

# a = np.array([1, 2, 3])
# print(a)
# print(type(a))

matrix = np.zeros((2,3))
print(matrix)

matrix1 = np.ones((2,3))
print(matrix1)

full_matrix = np.full((2,3),6)
print(full_matrix)

#identity Matrix
identity_matrix = np.identity(4)
print(identity_matrix)

eye_matrix = np.eye(3)
print(eye_matrix)

use_a_arange = np.arange(0, 10, 2)
print(use_a_arange)

