import random

names = input("Enter a string of names, having space b/w them, with no special characters: \n")

names = names.split(" ") #It splits the string into substrings by spaces and put them into a LIST
#print(names)

predict = random.randint(0, len(names)-1)

#print(f"Index is {predict}.")

#index = str(names[predict])
#index = str(predict)
print(f"{names[predict]}, will pay the bills.")

