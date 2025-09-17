class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_noses = 1
        # self.heart = num_heart

    def eat(self):
        print("can eat")

    def work(self):
        print("can work")

class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def flirt(self):
        print("can flirt")

    def work(self):
        super().work()
        print("can code")

male_1 = Male("kushagra")
male_1.eat()
male_1.flirt()
print("after using super() method we can access any attribute and method of base class from which the current class is inherited")
male_1.work()
print(male_1.num_eyes)
print(male_1.name)