# ENCAPSULATION ->
# In an object-oriented python programming, you can restrict access to methods and variables
# This can prevent the date being modified by accident and is known as encapsulation and
# it can be achieved using the private methods and variables
# Public Variable -> Accessible from anywhere
# Public Methods  -> Accessible from anywhere
# Private variable -> Accessible only in their  own methods
# Private Methods -> Accessible only in their own class or by a method if defined. starts with two underscores.


class myClass:
    __a = 10  # This is a private class variable. Scope is with in the class.

    def disp(self):
        print(self.__a)  # We need to use self keyword to access class variable


objM = myClass()
objM.disp()
