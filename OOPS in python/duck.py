class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    obj.quack()

# Creating instances of Duck and Person classes
duck = Duck()
person = Person()

# Passing instances to the make_it_quack function
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm quacking like a duck!
