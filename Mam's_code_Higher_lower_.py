import random
import os
import game_art
import game_database

print(game_art.game_logo)
score = 0
def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} , a {description} , from {country}"
def check_answer(guess, follower_1, follower_2):
    if follower_1 < follower_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return False
        else:
            return True
account_2 = random.choice(game_database.data)
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_1 = random.choice(game_database.data)
    while account_1 == account_2:
        account_2 = random.choice(game_database.data)
    print(f"Compare 1: {display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"Compare 2: {display_accountinfo(account_2)}")
    guess = int(input("who has more followers? Type 1 or 2 : "))
    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]
    is_correct = check_answer(guess, follower_count_1, follower_count_2)
    os.system("cls")
    print(game_art.game_logo)
    if is_correct:
        score += 1
        print(f"you are right. Your score is: {score}")
    else:
        print(f"you are wrong. Your score is: {score}")
        continue_flag = False
