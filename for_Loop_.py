# names = ['gauri', 'ladoo', 'aman']
#
# for names in names :
#     print(names)
#
# print()
# # print(names)


#my code
# numbers = [2, 3, 5, -2, 10]
# length = len(numbers)
# print(length)
# list2 = []
# count = 0
# l = 0
# for sq in numbers :
#     l = sq**2
#     count = count+1
#     print(l)
#     if count == length :
#         for item in l :
#          list2.append(item)
#          print(list2)


#gpt's code
# numbers = [2, 3, 5, -2, 10]
# length = len(numbers)  # number of items in the list
# list2 = []

# for sq in numbers:
#     l = sq**2
#     print(l)
#     if l == length:
#         list2.append(l)
#
# print(list2)

number = [2, 3, 5, -2, 10]
list1 = []
for i in number:
    list1.append(i**2)
    # sq = i ** 2
    # list1.append(sq)
print(list1)
