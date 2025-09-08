def multiply(*args):
    # c = []
    # for i in args:
    #     c.append(i)
    # print(c)
    c = 1
    for i in args:
        c *= i
    print(c)

multiply(2, 3, -6, 8)
multiply(2, 5, 8, 9, 0, 6)