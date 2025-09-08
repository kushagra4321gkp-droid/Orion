year = int(input("Enter the year : "))

if year % 4 == 0 :
    if year % 100 != 0 :
        print(f"{year} year is a leap year. ")
    elif year % 400 == 0 :
        print(f"{year} year is a leap year. ")
    else :
        print(f"{year} year is not a leap year. ")
else:
    print(f"{year} year is not a leap year. ")