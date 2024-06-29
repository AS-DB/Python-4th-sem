class computer:
    def __init__(self):
        self.name="Aditya"
        self.age=28

    def update(self,age):
        self.age=30
        print(age)

c1=computer()
c2=computer()

c2.name="sagar"
c2.age=100

print(c2.age)
print(c2.name)
print(c1.name)#its directly from init function
c1.update(21)

