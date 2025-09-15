#now we come to the advanced part of numpy
#we have to perform add, remove, split, stack
#we deal with the data which changes with time
#so we have to add new datapoint in the existing dataset
#we have to remove unnecessary data
#unlike list in which we can add, remove data anytime -> numpy arrays have fixed size
#if you have to perform any option like adding or removing so for that -> you have to create a new array
#n.insert(array, index, value, axis=None) -> used to insert an element in an array at specific index -> returns a new array
# -> original array will remain same. if none so it would a flattened array
#if axis = 0 -> insert data row wise
#if axis = 1 -> insert data column wise

import numpy as np

arr = np.array([[10, 20, 30, 40, 50, 60]])
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)

arr_2D = np.array([[1,2],[3,4]])
new_arr_2D = np.insert(arr_2D, 1, [5, 6], axis=0)
print(new_arr_2D)

#if you want to add an element to the array at the -> end
#np.append(arr, value)

#if you want to concatenate or join to arrays
#np.concatenate((array1, array2), axis = 0)
#axis = 0 -> vertical stacking
#axis = 1 -> horizontal stacking

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])

new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)
