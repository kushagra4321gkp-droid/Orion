import random

# from collections import deque

lives = 6
guess_list = ['apple', 'banana', 'pineapple', 'papaya', 'grapes']
random_guess = random.choice(guess_list)
# print(random_guess)


blank_list = []
for i in random_guess:
    blank_list.append('_')
print(blank_list)

print("guess the letters, You have only 6 lives in total.")

length = len(blank_list)

your_guess_stored = []

for i in range(length):
    your_guess = input("Guess the letters: ")
    your_guess_stored = your_guess.lower()
if your_guess_stored[i] != random_guess[i]:
    lives -= 1
    print("oh! Wrong guess, You have " + str(lives) + " lives left. Try again.")
elif your_guess_stored[i] == random_guess[i]:
    for j in blank_list:
        blank_list[i] = your_guess_stored[j]
        print("Well done, you have " + str(lives) + " lives left.")
print(blank_list)
final_guess = ''
for i in blank_list:
    final_guess = final_guess + i
print(final_guess)
if final_guess != random_guess:
    print("You Lost :(.")
else:
    print("You Win!")

# print(blank_list)
# print(random_guess)

# if random_guess[i] != blank_list[i] :
#     lives -= 1
#     print("You have " + str(lives) + " lives left.")
# elif random_guess == blank_list[i] :
#     print("Well done, you have " + str(lives) + " lives left.")
