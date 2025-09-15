import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1:3])
print(arr[2:])
print(arr[:])
print(arr[-1])                                #slicing means accessing subset of data

#fancy indexing = selecting multiple elements at once! pass multiple indices as a list
#use case = for non-sequencial values used more!
#what you select in the list as indices, it creates a copy

arr1 = np.array([10, 20, 30, 40, 50, 60])
print(arr1[[0, 2, 5]])