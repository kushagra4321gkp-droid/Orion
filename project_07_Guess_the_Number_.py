import random

print("let me think of a number between 0 and 50!")
random_number = random.randint(1, 50)
difficulty_level = input("choose level of difficulty...Type 'easy' or 'hard': ")
def winner_decider(yg, rg):
    if yg == rg:
        print(f"your guess {yg} is right")
        print("you won")
    if yg > rg:
        print("your guess is too high")
        print("Guess again")
    elif yg < rg:
        print("your guess is too low")
        print("Guess again")
def game():
    if difficulty_level == 'easy':
        for i in range(10,0,-1):
            print(f"you have {i} attempts remaining to guess the number")
            your_guess = int(input("Guess the number: "))
            winner_decider(yg=your_guess, rg=random_number)
            if your_guess != random_number and i == 0:
                print(f"you are out of guesses")
                print("You loose!")
                return

    elif difficulty_level == 'hard':
        for i in range(5,0,-1):
            print(f"you have {i} attempts remaining to guess the number")
            your_guess = int(input("Guess the number: "))
            winner_decider(yg=your_guess, rg=random_number)
            if your_guess != random_number and i == 0:
                print(f"you are out of guesses")
                print("You loose!")
                return

game()
