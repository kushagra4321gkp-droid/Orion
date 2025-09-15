import numpy as np

#reshaping means = to change the dimensions of an array without modifying it's data.
#for ex : 1D to 2D or 2D to 3D
#reshape(rows, columns) = specify new shape
#dimensions must match
#reshaping does not create a copy
#it returns a view
#changing value in the new shape will affect the array

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)



