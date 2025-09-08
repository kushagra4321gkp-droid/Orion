number = int(input('Enter a number: '))
product = 1
for i in range(1,number+1):
    if i <= number:
        product *= i
print(product)