import random

print("Your call")

predict = int(input("Enter your choice, (0/1) : "))

if predict == 0 or predict == 1:
    print("Valid input")

    a = random.randint(0, 1)

    print("The Result! After Toss ")

    print(a)

    if predict == a:
        print("You win :) ")
    elif predict != a:
        print("You lose :( ")
    else:
        print("Tie :| ")

    if a == 0 and predict == a:
        print("both Tails")
    else:
        print("both Heads")

else :
    print("Invalid input, choose either 0 or 1")