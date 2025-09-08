name = input("Enter your name: ")
full_name = name.split(" ")
def format_name(title):
    formated_name = ""
    for i in title:
        for j in range(len(i)):
            if j == 0:
                formated_name += i[j].upper()
            else :
                formated_name += i[j].lower()
        formated_name += " "
    print(formated_name)

format_name(title=full_name)