class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
    
    def show(self):
        print(self.name,self.roll)

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=8
        
        def display():
            print("Hello from inner class")

student.Laptop.display()