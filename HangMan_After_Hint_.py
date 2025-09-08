import random

lives = 6
guess_list = ['apple', 'banana', 'cherry', 'pineapple']
random_word = random.choice(guess_list)
i = 0
blank_list = []
for i in random_word:
    blank_list += '_'
print("HANGMAN GAME - YOU HAVE 06 LIVES")
print(blank_list)
game_over = False
while not game_over:
    guessed_letter = input("Guess the letters: ")
    for i in range(len(random_word)):  # 0 1 2 3 4 = a p p l e
        random_letter = random_word[i]
        if random_letter == guessed_letter:
            blank_list[i] = guessed_letter
    print(blank_list)
    if guessed_letter not in blank_list:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
    if '_' not in blank_list:
        game_over = True
        print("You Won!")
print(random_word)
