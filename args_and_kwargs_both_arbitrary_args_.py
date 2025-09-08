def myinfo(height,*args,**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    for i in args:
        print(i)
    print(kwargs['name'])
    #print(args[0])
    print(f"height is {height}")
    print(f"tuple is {args}")
    print(f"dict is {kwargs}")


myinfo('ai',name='aman',age=18,proffesion='student')
myinfo('ml',name='savita',proffesion='business')
myinfo('cs',age=30,name='jenny',)