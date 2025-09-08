import os


def calculate(f, o, n):
    if o == '+':
        result = f + n
        print(f"{f} + {n} = {result}")
    elif o == '-':
        result = f - n
        print(f"{f} - {n} = {result}")
    elif o == '*':
        result = f * n
        print(f"{f} * {n} = {result}")
    elif o == '/':
        result = f / n
        print(f"{f} / {n} = {result}")
    return result


fn = int(input("enter first number : "))
op_list = ['+', '-', '*', '/']
for i in op_list:
    print(i)
op = input("pick an operation : ")
nn = int(input("enter next number : "))
result1 = calculate(f=fn, o=op, n=nn)
# print(result1)
choice = input("enter 'y' to continue with the result or enter 'n' to restart or enter 'x' to exit : ")
end = True
while end:
    if choice == 'y':
        op = input("pick an operation : ")
        nn = int(input("enter next number : "))
        result1 = calculate(f=fn, o=op, n=nn)
        fn = result1
        print(calculate(f=fn, o=op, n=nn))
        # print(f"{fn}{op} = {calculate(f=fn,o=op,n=nn)}")
    elif choice == 'n':
        os.system('cls')
        fn = int(input("enter first number : "))
        op = input("pick an operation : ")
        nn = int(input("enter next number : "))
        print(calculate(f=fn, o=op, n=nn))
        # print(f"{fn}{op} = {calculate(f=fn, o=op, n=nn)}")
    elif choice == 'x':
        end = False
    choice = input("enter 'y' to continue with the result or enter 'n' to restart or enter 'x' to exit : ")
