set1 = {10, 56, 89, 90, 'savita', True}
print(type(set1))
print(set1)
print(set1)
print(set1)
print(set1)

set2 = {10, 56, 89, 90, 'savita', True, 9, 1, 8, 'aman'}
print("\n",set2) #True and 1 are duplicate values

set2.add(2)
print(set2)

set2.remove(True)
print(set2)

# set2[2] = 1000
# print(set2) set is unchangeable, indexing is also not possible, duplicate values are not allowed.

# x = [1, 2, 3]
# y = x   # Is this a copy or a reference? (You have to know Python’s internals)
# print(x)
# print(y)
#
# x = [1, 2, 3]
# y = x.copy()   # Very clear: y is a copy of x
# print(x)
# print(y) #Explicit is better than implicit.