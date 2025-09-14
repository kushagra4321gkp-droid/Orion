import numpy as np

arr_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2D.shape)

#size will return total number of elements
print(arr_2D.size)

print("printing dimension below")
find_ndim = np.ndim(arr_2D)
print(find_ndim)

print("4 dimensional array")
arr_4D = np.array([[[[1,2],[3,4],[5,'savita'],[7,8]]]])
# print(arr_4D.shape)
# print(arr_4D.size)
print(arr_4D.ndim)

#dtype is used to tell datatype of the elements present in the array
print(arr_4D.dtype)

arr_4D.astype(str)
print(arr_4D.dtype)