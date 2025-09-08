class Car:
    def drive(self):
        print("Vroom")

print(type(Car))
print(type(type))

# car1  ---> instance of Car
# Car   ---> instance of type
# type  ---> instance of type (it’s self-referential 🤯)

print(type(sorted))

a = 256
b = 256

print(a is b)

c = 257
d = 257

print(c is d)