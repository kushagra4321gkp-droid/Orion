his_name = input("What's his/your name? : ")
her_name = input("What's her/your name? : ")

his_name_in_Lowercase = his_name.lower()
her_name_in_Lowercase = her_name.lower()

t1 = his_name_in_Lowercase.count("t")
r1 = his_name_in_Lowercase.count("r")
u1 = his_name_in_Lowercase.count("u")
e1 = his_name_in_Lowercase.count("e")
l1 = his_name_in_Lowercase.count("l")
o1 = his_name_in_Lowercase.count("o")
# e1 = his_name_in_Lowercase.count("e")
v1 = his_name_in_Lowercase.count("v")

t2 = her_name_in_Lowercase.count("t")
r2 = her_name_in_Lowercase.count("r")
u2 = her_name_in_Lowercase.count("u")
e2 = her_name_in_Lowercase.count("e")
l2 = her_name_in_Lowercase.count("l")
o2 = her_name_in_Lowercase.count("o")
# e2 = her_name_in_Lowercase.count("e")
v2 = her_name_in_Lowercase.count("v")

# print(t1)
# print(r1)
# print(u1)
# print(e1)
# print(l1)
# print(o1)
# print(v1)

add1 = t1 + r1 + u1 + e1 + t2 + r2 + u2
add2 = l1 + o1 + v1 + e1 + l2 + o2 + v2

# print(add1)
# print(add2)

print(f"The Final percentage is {add1}{add2}")


