class Instructor:

    follower_count = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def dispplay(self, sub):
        print(f"Hi my name is {self.name} and I teach {sub}")

    def FollowerCount(self):
        self.follower_count +=1
        print(f"Hi my name is {self.name} and I have {self.follower_count} followers")

instructor_1 = Instructor('Jenny', 'Delhi')
print(instructor_1.name)
print(instructor_1.address)
instructor_1.dispplay('python')
instructor_1.FollowerCount()
instructor_1.FollowerCount()

