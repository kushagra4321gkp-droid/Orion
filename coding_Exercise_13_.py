list1 = [['😃'], ['😃'], ['😃']]
list2 = [['😃'], ['😃'], ['😃']]
list3 = [['😃'], ['😃'], ['😃']]

print(list1)
print(list2)
print(list3)

print("Where you want to hide your money? ")

row_position = int(input("Enter the row position: "))
column_position = int(input("Enter the column position: "))

if row_position == 1 :
    list1[column_position-1][0] = '💸'
elif row_position == 2 :
    list2[column_position-1][0] = '💸'
elif row_position == 3 :
    list3[column_position-1][0] = '💸'
else :
    print("Please enter a valid row position!")

if row_position == 1 or row_position == 2 or row_position == 3 :
    print(list1)
    print(list2)
    print(list3)













# list[column_position][0] = 'x'