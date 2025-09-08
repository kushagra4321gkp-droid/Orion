# a = 10 #global
# def display():
#     a = 15 #local
#     print(a)
# display()

# a = 10 #global
# def display():
#     a = 15 #local
#     print(a)
#     def show():
#         print(a)
#     show()
# display()

# a,b = 6,5
# def display():
#     if a > b:
#         c = a + b
# print(c)

name = "Jenny's"
def display():
    global name
    name += " Lecture"
print(name)
display()
print(name)





