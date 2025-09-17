class Human:
    def __init__(self, has_heart):
        self.num_eyes = 2
        self.num_noses = 1
        self.has_heart = has_heart
                                                # ⣏⡉ ⡀⢀ ⣀⡀ ⡇ ⢀⣀ ⣀⡀ ⢀⣀ ⣰⡀ ⠄ ⢀⡀ ⣀⡀
                                                # ⠧⠤ ⠜⠣ ⡧⠜ ⠣ ⠣⠼ ⠇⠸ ⠣⠼ ⠘⠤ ⠇ ⠣⠜ ⠇⠸

        #Here I am initializing that whatever the object of Human we create, it will ask for an argument in the constructor, so either we pass the value of has_heart at the time of object creation of the class Human. or we have other option as well.

        #Here what I am doing is since I have created a new class male
        #And I am inheriting Human class via Male class. So there is another way to pass the value of has_heart

        #Since I felt the need for Male class's own attributes so i used Male's Init() special function which is used to initialize Male class's object.
        #and since i used init() in Male and Male is Inheriting Human so Male's init() overrode Human's init()
        #so now Male is not inheriting any attribute of its parent class
        #to keep inheriting, we have to use super().__init__()

        #It will help us to keep the inherited attribute and add extra attribute that Male's object can possess
        #Now since Male's init() is overriding Human's init(), and Human's init() is asking for one argument from Male's init()
        #and since Male's init() is also a initializer, it will ask for the same thing from the object of Male class.

        #so we create object of Male class, we pass positional argument, then that argument is passed to the Male's init() as parameter, then that parameter is pass as the argument to super().__init__() 's parameter , which is Human's init()
        #now Human's init() will initialize that attribute has_heart according to the user
        #now object can get initialized just by passing positional argument for has_heart attribute in the Male's Constructor while creating object

        #main purpose of Inheritance is Reusability of Code

    def eat(self):
        print("can eat")

    def work(self):
        print("can work")

class Male(Human):
    def __init__(self,has_heart,name):
        super().__init__(has_heart)
        self.fight = True
        self.name = name
    
    def work(self):
        super().work()
        print("can brainStorm")

    def display(self):
        return f"I am {self.name} and I have {self.has_heart} heart"

male_1 = Male(1,"Kushagra Tiwari")
male_1.eat()
male_1.work()
print(male_1.num_noses)
print(male_1.num_eyes)
print(male_1.fight)
print(male_1.name)
print(male_1.display())

h = Human(1)
print(h.has_heart)

# Same Explanation : I asked chatgpt to covert above RAW explanation into decorative one : But you know RAW is RAW ;) Good Luck
# 🧩 Human Class Initialization:
# 👉 Whenever we create an object of Human, it will ask for an argument in the constructor.
#    That argument is `has_heart`. So we must pass it at object creation.
#    (Either directly when making Human OR indirectly via inheritance).

# 🧑‍🤝‍🧑 Inheriting with Male:
# 👉 I created a new class `Male`, inheriting from `Human`.
#    This gives me another way to pass the value of `has_heart`.

# ⚙️ Why redefine __init__ in Male?
# 👉 Because I wanted Male to have its own attributes (like `name`, `fight`).
# 👉 But since Male’s `__init__()` overrides Human’s `__init__()`,
#    Male would stop inheriting attributes from Human.
# 🚀 Solution → Use `super().__init__()` to still call Human’s constructor.

# 🔄 How it works:
# 1️⃣ Create an object of Male → pass a positional argument (e.g., 1 for `has_heart`).
# 2️⃣ That value goes into Male’s constructor (`__init__`).
# 3️⃣ Male passes it to `super().__init__()` → calls Human’s constructor.
# 4️⃣ Human initializes `has_heart` for Male too ✅.

# 🎯 Final Outcome:
# 👉 Male objects now keep all Human attributes + add their own attributes.
# 👉 So we achieve *code reusability* and extend functionality.

# 🌟 Main purpose of Inheritance → **Reusability of Code**
