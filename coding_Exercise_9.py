height = int(input("Enter your height: "))

if height >= 3 :
    print(f"Your height is {height}, you can ride.")
    age = int(input("Enter your age: "))

    if age < 12 :
        print(f"Your age is {age}, pay 150 rs.")
        total = 150
        take_Photos = input("Do you want to take photos? (y/n): ")
        if take_Photos == "y" :
            print("Pay extra 50rs")
            total += 50
        else :
            print("Good Luck")
    elif age < 18 :
        print(f"Your age is {age}, pay 250 rs.")
        total = 250
        take_Photos = input("Do you want to take photos? (y/n): ")
        if take_Photos == "y" :
            print("Pay extra 50rs")
            total += 50
        else :
            print("Good Luck")
    else :
        print(f"Your age is {age}, pay 500 rs.")
        total = 500
        take_Photos = input("Do you want to take photos? (y/n): ")
        if take_Photos == "y" :
            print("Pay extra 50rs")
            total += 50
        else :
            print("Good Luck")
    print(f"Your Total bill is {total}.\nThanks for visiting.")
else :
    print(f"Your height is {height} which is less than 3 so you can not ride.")

