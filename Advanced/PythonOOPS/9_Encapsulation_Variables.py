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
    # This is private as it started with two underscores
    b = 20  # this is a public class variable

    def disp(self):
        print(self.__a)  # We need to use self keyword to access class variable.


print("##########################(1)################################")
objM = myClass()
objM.disp()
# print(myClass.__a)  # Here we cannot access private variable outside the class. We will get attribute error
print(myClass.b)  # We can access this as it is not a private variable
print("#############(2-Accessing private variables outside of the class indirectly using methods)#############")


class A:
    __i = 20  # It is a private variable

    def dispI(self):
        print(self.__i)

    def getI(self, ivalue):
        self.__i = ivalue
        print(self.__i)


obj = A()
obj.dispI()  # Here it is 20
obj.getI(30)  # Here indirectly we accessed a private variable
obj.dispI()  # Here it is 30 as it was accessed and modified using the above method
