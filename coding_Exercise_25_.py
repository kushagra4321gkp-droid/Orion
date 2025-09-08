year = int(input("Enter a year: "))
def month_days(y):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
        return {
        'jan':31,
        'feb':29,
        'mar':31,
        'apr':30,
        'may':31,
        'jun':30,
        'jul':31,
        'aug':31,
        'sep':30,
        'oct':31,
        'nov':30,
        'dec':31,
        }
    else:
        print(f"{year} is not a leap year")
        return {
            'jan':31,
            'feb':28,
            'mar':31,
            'apr':30,
            'may':31,
            'jun':30,
            'jul':31,
            'aug':31,
            'sep':30,
            'oct':31,
            'nov':30,
            'dec':31,
        }
print(month_days(y=year))