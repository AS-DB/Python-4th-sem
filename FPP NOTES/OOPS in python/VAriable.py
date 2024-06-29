class car:
    wheels=10
    def __init__(self):
        self.mil=10
        self.com="BMW"
c1=car()
c2=car()

print(c1.com,c2.com,c1.wheels)

c1.com=100
print(c1.com,c2.com,c2.wheels)



