class Rectangle:

    hi = 'hi'

    def __init__(self, length=5, breadth=5):
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth), Rectangle.hi

rectangle = Rectangle(4,5)
print(rectangle.perimeter())
print(rectangle.area)