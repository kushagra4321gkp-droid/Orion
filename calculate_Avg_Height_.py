height = input("Enter list of height : ")
height_list = height.split(',')
print(height_list)
count = 0
for i in height_list:
    count = count + 1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
print(height_list)
sum = 0
for i in height_list:
    sum = sum + i
print(sum)
avg = sum / count
print(avg)
print(round(avg))
