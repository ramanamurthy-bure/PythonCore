# Creating constructor within the abstract class

from abc import ABC, abstractmethod


class Cal(ABC):

    def __init__(self, value):  # This is a constructor in python
        self.value = value

    @abstractmethod  # this is qualifier to make a method as abstract method
    def add(self):  # abstract method
        pass

    @abstractmethod  # this is qualifier to make a method as abstract method
    def sub(self):  # abstract method
        pass


class C(Cal):  # child class of abstract class Cal
    def add(self):  # abstract method implementation
        print("Add method implementation", self.value + 50)

    def sub(self):  # abstract method implementation
        print("Sub method implementation", self.value - 40)


objc = C(10)
objc.add()  # 60
objc.sub()  # -30
