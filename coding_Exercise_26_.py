class Calculator:
    def __init__(self, rad):
        self.rad = rad
    def area(self):
        area = 3.14 * (self.rad ** 2)
        print(f"Area of circle is {area} meter sq")
    def circumference(self):
        circumference = 2 * 3.14 * self.rad
        print(f"Circumference of circle is {circumference} meter")

radius = int(input("Enter radius: "))
CalC = Calculator(rad=radius)
CalC.area()
CalC.circumference()
