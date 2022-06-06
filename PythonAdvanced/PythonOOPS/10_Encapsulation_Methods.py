# ENCAPSULATION ->
# In an object-oriented python programming, you can restrict access to methods and variables
# This can prevent the date being modified by accident and is known as encapsulation and
# it can be achieved using the private methods and variables
# Public Variable -> Accessible from anywhere
# Public Methods  -> Accessible from anywhere
# Private variable -> Accessible only in their own class
# Private Methods -> Accessible only in their own class or by a method if defined. starts with two underscores.


class myClass:

    def __disp1(self):  # This is a private method. This can be accessed with the class by another public method
        print("This is a private method accessed by public method disp2...")

    def disp2(self):  # This is a public method
        print("This is a public method...")
        self.__disp1()  # This is how we can call private method. Like class variable accessing we need to use self keywork
        #  to access method also


obj = myClass()
obj.disp2()  # We can only call disp2() as it is public method
obj.__disp1()  # We cannot call as it is a private method. We will get 'AttributeError'


