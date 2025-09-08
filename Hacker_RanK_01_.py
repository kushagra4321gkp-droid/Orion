n = int(input("Enter any number : "))
if n % 2 != 0 :
    print("Weird")
elif n % 2 == 0 :
    if 2 <= n <= 5 or n > 20:
        print("Not Weird")
    elif 6 <= n <= 20 :
        print("Weird")