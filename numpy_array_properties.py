import numpy as np

arr_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2D.shape)

#size will return total number of elements
print(arr_2D.size)

print("printing dimension below")
find_ndim = np.ndim(arr_2D)
print(find_ndim)