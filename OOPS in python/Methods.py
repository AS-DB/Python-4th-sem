class student:
    school ="GIET"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):#instanseous method
        return ((self.m1+self.m2+self.m3))/3
#accesors
    def get(self,a):
        return self.a
#mutators
    def set(self,a):
        self.a=10
#class method
    @classmethod
    def ageq(cls):
        cls.age += 1
        return cls.age
    
    age=100
#statc method
    def add(x,y):
        return x+y
    
print(student.school)
s1=student(10,20,30)
print(s1.avg())#instance method
#class method
print(student.ageq())
