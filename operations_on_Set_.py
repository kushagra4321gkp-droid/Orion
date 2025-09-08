set1 = {'aman', 'savita', 'ladoo', 'gauri'}
set2 = {'satish', 'payal', 'smay', 'ladoo'}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

#set1 = set()

print(set1.union(set2,(1, 3, 100)))
print(set1 | set2)

#print(set1)

set1.intersection_update(set2)
print(set1)
