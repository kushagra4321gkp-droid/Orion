number = int(input("Enter any number : "))
count = 0
for i in range(1, number):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        count += 1
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print(f"number of FizzBuzz in this series is {count}")