#to remove elements from an array we use delete()
#np.delete(array, index, axis=None)
#no inplace removal like list
#always creates a new array
#1:31:06

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
nw_arr = np.delete(arr, 0, axis=0)
print(nw_arr)

arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
new_arr_2D = np.delete(arr_2D, 0, axis=0)
print(new_arr_2D)