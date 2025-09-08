import game_database
import random
randomly_choosen1 = random.choice(game_database.data)
index_is = game_database.data.index(randomly_choosen1)
game_database.data.pop(index_is)
randomly_choosen2 = random.choice(game_database.data)
your_score = 0
print(f"you are right, your score is {your_score}")
Higher_Lower_Ascii = r"""                                                                                                
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                    """
print(Higher_Lower_Ascii)
personalities_in_tuple1 = tuple(randomly_choosen1.values())
clear_1 = " , ".join(map(str, personalities_in_tuple1))
personalities_in_tuple2 = tuple(randomly_choosen2.values())
clear_2 = " , ".join(map(str, personalities_in_tuple2))
print(f"Compare 1 : {clear_1}")
verses = r"""
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ """
print(verses)
print(f"Compare 2 : {clear_2}")
you_Typed = input("Who has more followers? Type '1' or '2' : ")
game_not_end = True
while game_not_end :
    you_Typed = input("Who has more followers? Type '1' or '2' : ")
    def when_right_then_increment():
        your_score = 0
        if randomly_choosen1["follower_count"] > randomly_choosen2["follower_count"] and you_Typed == "1":
            your_score = your_score + 1
            game_not_end = True
        elif randomly_choosen1["follower_count"] < randomly_choosen2["follower_count"] and you_Typed == "2":
            your_score = your_score + 1
            game_not_end = True
        elif randomly_choosen1["follower_count"] < randomly_choosen2["follower_count"] and you_Typed == "1":
            print("you lost")
            game_not_end = False
        elif randomly_choosen1["follower_count"] < randomly_choosen2["follower_count"] and you_Typed == "2":
            print("you lost")
            game_not_end = False
        else :
            print("enter valid input")
        return your_score
    your_score = when_right_then_increment()
    print(your_score)


