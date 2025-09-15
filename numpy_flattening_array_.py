import numpy as np

#if you want to convert multidimensional array into 1D array
#.ravel() -> returns a view -> original array modification
#.flatten() -> returns a copy -> no original array modification

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ravel())
print(arr.flatten())
