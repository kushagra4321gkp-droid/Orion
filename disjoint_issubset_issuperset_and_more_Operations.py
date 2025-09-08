# set1 = {'satish', 'ladoo', 0, 3.3}
# set2 = {'gauri', 'savita', 20, 16, True}
# print(set1.isdisjoint(set2))

# set1 = {'satish', 'ladoo', 0, 3.3} #set is a subset of set2
# set2 = {'gauri', 'savita', 20, 16, True,'satish', 'ladoo', 0, 3.3} #set2 is a superset
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
# print(set1.issubset(set2))

set1 = {'Ram', 'Shyam', 'jenny'}
set2 = {'Jiya', 'akash'}
print(set1.issubset(['Ram', 'Shyam', 'jenny', 'Mohan', 'shiva']))
print(set1 <= set2)
print(set1 <= set1)

