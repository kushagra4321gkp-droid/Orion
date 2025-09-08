n = int(input("Enter a number: "))
num = 2
while num < n:
    if n % num != 0:
        num += 1
    else:
        print("Not a prime number")
        break
    print("prime")