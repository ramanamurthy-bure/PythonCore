# ABSTRACT CLASS ->
# Abstract classes are classes that contain one or more abstract methods
# An abstract method is a method that is declared, but contains no implementation
# Abstract classes cannot not be instantiated, and require subclasses to provide implementations
# for the abstract methods
# Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class
# ABC is pre-defined abstract class present in python. We need to import it from package abc
# To create a abstract class we need to use this pre-defined class
from abc import ABC, abstractmethod


class A(ABC):  # ABC is pre-defined abstract class present in python. Now class A becomes abstract class

    @abstractmethod  # We need to specify this qualifier to make particular method abstract
    def disp(self):
        None  # No implementation for this method in this class. This is what abstract class.


class B(A):
    def disp(self):
        print("This is implementation for the abstract method of- class A")
        # abstract method implementation should be there in the child class


# We cannot create object for abstract class objA = A() is not possible
objb = B()
objb.disp()







