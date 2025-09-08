# a = range(5)
# print(list(a))

# r = range(1_000_000_000)  # A billion numbers!
# print(list(r))  # Still works instantly Risky code don't ever run

sum = 0
for i in range(1, 101):
    sum += i
    print(sum)
print(f"The total sum of 1 to 100 numbers is : {sum}")
