import random
#Easy password generator
# letter = int(input("Enter count of letters : "))
# symbol = int(input("Enter count of symbol : "))
# number = int(input("Enter count of numbers : "))
# letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','Z']
# symbol_list = ['@', '#', '$', '^', '*', '(', ')', '!', '?', ':', '<', '>', '"', '{', '.', '[', '}', '|', '`', '~']
# count1 = letter
# count2 = symbol
# count3 = number
# random_number = ''
# random_symbol = ''
# random_letter = ''
# for i in range(1, count1):
#     a = random.choice(letter_list)
#     random_letter += a
# for j in range(1, count2):
#     b = random.choice(symbol_list)
#     random_symbol += b
# for k in range(1, count3):
#     c = str(random.randint(1, number))
#     random_number += c
# print(f"Your password is {random_number}{random_symbol}{random_letter}")

#Hard password generator
letter = int(input("Enter count of letters : "))
symbol = int(input("Enter count of symbol : "))
number = int(input("Enter count of numbers : "))
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','Z']
symbol_list = ['@', '#', '$', '^', '*', '(', ')', '!', '?', ':', '<', '>', '"', '{', '.', '[', '}', '|', '`', '~']
count1 = letter
count2 = symbol
count3 = number
random_number = []
random_symbol = []
random_letter = []
for i in range(1, count1+1):
    a = random.choice(letter_list)
    random_letter.append(a)
for j in range(1, count2+1):
    b = random.choice(symbol_list)
    random_symbol.append(b)
for k in range(1, count3+1):
    c = str(random.randint(1, number))
    random_number.append(c)
# print(random_number)
# print(random_symbol)
# print(random_letter)
password_list = random_letter + random_number + random_symbol
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ''
for i in password_list:
    password += i
print(password)


