# number = int(input("Enter a number (-1 to quit) : "))
# while number != -1:
#     print(number)
#     number = int(input("Enter a number (-1 to quit) : "))
# else:
#     print("in the else block")
# print("out from the while loop")

                #DOUBT ask chatGPT
#Enter a number (-1 to quit) : 7445
# 7445
# Enter a number (-1 to quit) :
# Traceback (most recent call last):
#   File "C:\Users\kusha\PycharmProjects\PythonProjectFirst\while_loop_.py", line 4, in <module>
#     number = int(input("Enter a number (-1 to quit) : "))
# ValueError: invalid literal for int() with base 10: ''
#
# Process finished with exit code 1
# 5

                          #DOUBT ask chatGPT
# count = 1
# while True:
#     print(count)
#     count += 1
#     if print(False): #Now this is an infinite loop
#         break
# else:
#     print("in else block")
# print("out of the loop")


# total = 0
# numbers = int(input("Enter the number: "))
# while numbers != -numbers or numbers != -(numbers) or numbers != +(-numbers) or numbers != -(+numbers):
#     if numbers == -numbers or numbers == -(numbers) or numbers == +(-numbers) or numbers == -(+numbers):
#         total += 0
#     total = total + numbers
#     print(total)
#     numbers = int(input("Enter the number: ")) #Why my program does not considering - (minus) sign, i wrote - to signify negative number, why python ignores that?
#     if numbers == 0:
#         break

                   # mam's code
total = 0
number = int(input("Enter a number: "))
while number != 0:
    total = total + number
    number = int(input("Enter a number: "))
print(total)
