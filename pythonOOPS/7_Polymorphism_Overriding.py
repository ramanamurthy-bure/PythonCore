# POLYMORPHISM -> This can be achieved using method overloading and method overriding
# sometimes an object comes in many types or forms
# if we have a button, there are different draw outputs(round button, check button,
# square button, button with image. But they do share the same logic - onClick()
# We access them using the same method. This idea is called Polymorphism

# METHOD OVERRIDING
# Override means having two methods with same name but doing different task
# It means one of the methods overrides the other
# If there is any method in the superclass and a method with same name in a subclass, then by executing the method
# of the corresponding class will be executed

# Overriding can be used for a variable and method

# Overriding a variable
print("##########################(Overriding a variable)################################")


class A:
    name = "Ramana"

    def m1(self):
        pass


class B(A):
    name = "Bure"

    def m2(self):
        pass


objb = B()
print(objb.name)  # Here we will get output as 'Bure' as the variable
# in child class B will override the variable in parent class as both are having same name
# This we call as a variable overriding in python
print("##########################(Overriding a method)################################")


class Bank:
    def rateofinterest(self):
        return 0


class ICICI(Bank):
    def rateofinterest(self):
        return 10.5


objICICI = ICICI()
print(objICICI.rateofinterest())

objBank = Bank()
print(objBank.rateofinterest())
