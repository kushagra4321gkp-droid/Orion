class Instructor :
    def __init__(self, name):
        self.name = name
        self.age = 0

    def doteach(self):
        print("Teaching")

instructor_1 = Instructor("Kushagra" )

instructor_1.doteach()