import random

user_choice = int(input("Enter your choice, (0/1/2) : "))

if user_choice >= 3 and user_choice < 0:  # "3 <= user_choice < 0" also fine- It says simplify chained comparison
    print("Enter a valid choice, You Lose!")
else:
    computer_choice = random.randint(0, 2)

    if user_choice == 0:
        print('You choose rock : 🌑')
    elif user_choice == 1:
        print('You choose paper : 📃')
    elif user_choice == 2:
        print('You choose scissors : ✂️')
    else:
        print("Enter a valid choice, You Lose!")

    if computer_choice == 0:
        print('Computer choose rock : 🌑')
    elif computer_choice == 1:
        print('Computer choose paper : 📃')
    elif computer_choice == 2:
        print('Computer choose scissors : ✂️')

    if user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("Enter a valid choice, You Lose!")
