class Animal():  # Base class
    # Constructor
    def __init__(self):
        print("Animal created!")

    # Method
    def who_am_i(self):
        print('I am an Animal')

    # Method
    def eat(self):
        print('I am eating')


class Dog(Animal):  # Derived class

    # Constructor
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof!")

    def eat(self):  # This will override the eat method in the base class
        print("I am a dog and eating")


my_dog = Dog()
# Here we can access base class methods using the derived class instance like below
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

# Polymorphism
# Refers the way in which different object classes can share the same name
