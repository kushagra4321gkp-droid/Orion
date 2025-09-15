import numpy as np

arr2 = np.array([10, 20, 30, 40, 50, 60])

 #boolean masking used in machine leaning to filter the data
 #it returns the value on the behalf of the condition you provide
 #it is 10 times faster than loops

print(arr2[arr2 > 20])