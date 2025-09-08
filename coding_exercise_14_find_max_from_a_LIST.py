list1 = input("Enter a list of numbers: ")
list2 = list1.split(",")
print(list2)
count = 0
for i in list2:
    count = count + 1
print(count)
for i in range(count):
    list2[i] = int(list2[i])
print(list2)
maxi = list2[0]
for number in list2:
    if number > maxi:
        maxi = number
else:
    print(f"maximum number is : {maxi}")

