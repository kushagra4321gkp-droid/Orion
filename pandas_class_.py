import pandas as pd

df = pd.DataFrame({
    'A1' : [1, 2, 3],
    'B2' : [True, True, False],
    'C3' : [0.496714, 0.2344, -1.4553234]},
    index = ['a', 'b', 'c']
    )
print(df)

a = 4
print(a)
# a = a + 4
a += 4
print(a)

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print('done')

spirit = print
spirit("how")

a = 10
def show():
    print(a)
def display():
    a = 95
    show()
display()
print("how")

a = 5
print(type(type))




