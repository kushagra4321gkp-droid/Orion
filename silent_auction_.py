# welcome = "******* Welcome to Silent Auction Program *******"
# print(welcome)
# name = input("Enter your name: ")
# bid = input("Enter your bid: ")
# continue1 = input("Do you want to continue? (y/n)")
# dict1 = {}
# while continue1 == "y":
#     dict1[name] = input("Enter your name: ")
#     dict1[bid] = input("Enter your bid: ")
#     bids =[]
#     for i in dict1.values():
#         bids.append(i)
#     print(bids)
#     bids.sort()
#     big = 0
#     for i in bids:
#         big = i
#     print(big)
import os
def find_winner(dict1):
    for i in dict1: # {jenny:2929, ram:3798, gauri:8999}
        bids = dict1[i]
        winner = ''
        highest_bid = 0
        if bids > highest_bid:
            highest_bid = bids
        winner = i
    print(f"winner is {winner} with bid of {highest_bid}")



dict1 = {}
continue1 = 'yes'
while continue1:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    dict1[name] = bid
    continue_or_not = input("Do you want to continue or not? (yes/no): ")
    if continue_or_not == "yes":
        os.system('cls')
    if continue_or_not == "no":
        continue1 = False
        find_winner(dict1)

print(dict1)



