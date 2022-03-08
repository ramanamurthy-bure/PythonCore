# In python child class must do implementation for all the abstract methods from its abstract class
# only then it will allow creating object
from abc import ABC, abstractmethod


class Animal(ABC):  # ABC is pre-defined abstract class present in python. Now class A becomes abstract class

    @abstractmethod  # We need to specify this to make particular method abstract
    def eat(self):
        None  # No implementation for this method in this class. This is what abstract class.


class Tiger(Animal):
    def eat(self):
        print("Eat NON-VEG")
        # abstract method implementation should be there in the child class


class Cow(Animal):
    def eat(self):
        print("Eat VEG")
        # abstract method implementation should be there in the child class


objt = Tiger()
objt.eat()

objc = Cow()
objc.eat()






