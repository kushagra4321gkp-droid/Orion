total = 0
enter_size = input("Enter the size of your pizza, (s,m,l) : ")
if enter_size == "s" :
    print("pay 100 rs")
    print(f"Your total bill is {total}.")
elif enter_size == "m" :
    print("pay 200 rs")
    print(f"Your total bill is {total}.")
    print("enjoy Your pizaa")
elif enter_size == "l" :
    print("pay 300 rs")
    print(f"Your total bill is {total}.")
    print("enjoy Your pizaa")
else :
    print("wrong choice")


# For pepperoni pizza

pep_Size = input("Do you want pepperoni pizza then enter your choice, (s,m,l) : ")
if pep_Size == "s":
    print("pay extra 30 rs")
    print(f"Your total bill is {total}.")
    print("enjoy Your pepperoni pizaa")
elif pep_Size == "l" or pep_Size == "m" :
    print("pay 50 rs extra")
    print(f"Your total bill is {total}.")
    print("enjoy Your pepperoni pizaa")


# For Extra Cheese

extra_cheese = input("Do you want Extra Cheese?, (y/n) : ")
if extra_cheese == "y" :
    print("pay 20 rs extra")
    print(f"Your total bill is {total}.")
    print("enjoy Your pizza with extra cheese")
else :
    print("enjoy Your pizaa with no cheese.")
print(f"Your total bill is {total}")


    
    
    
    