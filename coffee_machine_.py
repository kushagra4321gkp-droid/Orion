from coffee_resources import ingredients


def resources(ingred, rupees, which_coffee):
    if rupees >= 89:
        if which_coffee == 'espresso' and ingred["milk"] >= 150 and ingred["water"] >= 60 and ingred["coffee"] >= 20:
            return which_coffee
        elif which_coffee == 'latte' and ingred["milk"] >= 120 and ingred["water"] >= 89 and ingred["coffee"] >= 15:
            return which_coffee
        elif which_coffee == 'cappuccino' and ingred["milk"] >= 133 and ingred["water"] >= 99 and ingred[
            "coffee"] >= 23:
            return which_coffee
        else:
            if ingred["milk"] < 120:
                print("Sorry! there is not enough milk")
            elif ingred["water"] < 60:
                print("Sorry! there is not enough water")
            elif ingred["coffee"] < 10:
                print("Sorry! there is not enough coffee")
    else:
        print(f"Sorry! that's not enough money. Money refunded {rupees}")
    return 'no'


def take_the_change(coffeee, five_rupee, ten_rupee, twenty_rupee):
    if coffeee == "latte":
        latte_price = 89
        total_rupee1 = (five_rupee * 5) + (ten_rupee * 10) + (twenty_rupee * 20)
        if total_rupee1 > latte_price:
            return total_rupee1 - latte_price, total_rupee1
    elif coffeee == "cappuccino":
        cappuccino_price = 75
        total_price2 = (five_rupee * 5) + (ten_rupee * 10) + (twenty_rupee * 20)
        if total_price2 > cappuccino_price:
            return total_price2 - cappuccino_price, total_price2
    elif coffeee == "espresso":
        espresso_price = 99
        total_price3 = (five_rupee * 5) + (ten_rupee * 10) + (twenty_rupee * 20)
        if total_price3 > espresso_price:
            return total_price3 - espresso_price, total_price3
    total_price = (five_rupee * 5) + (ten_rupee * 10) + (twenty_rupee * 20)
    return 0, total_price


end_customer = True
while end_customer:
    coffee_type = input("what would you like to have? latte or cappuccino or espresso?: ")
    if coffee_type == "off":
        print("turned off")
        end_customer = False
        break
    print("Please insert the coins")
    five_rs = int(input("How many 5Rs. coins:? : "))
    ten_rs = int(input("How many 10Rs. coins:? : "))
    twenty_rs = int(input("How many 20Rs. coins:? : "))
    change, money = take_the_change(coffeee=coffee_type, five_rupee=five_rs, ten_rupee=ten_rs, twenty_rupee=twenty_rs)
    print(f"Here is your {change}Rupees change")
    print(f"Here is your {resources(ingred=ingredients, rupees=money, which_coffee=coffee_type)} coffee")


