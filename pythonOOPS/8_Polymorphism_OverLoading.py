# POLYMORPHISM -> This can be achieved using method overloading and method overriding
# sometimes an object comes in many types or forms
# if we have a button, there are different draw outputs(round button, check button, square button, button with image)
# but they do share the same logic - onClick()
# We access them using the same method. This idea is called Polymorphism

# METHOD OVERLOADING
# In python we can define a method such a way that there are multiple  ways to call it.
# Given a single method or function, we can specify the number of parameters  our self.

print("##########################(Overloading a method)################################")


class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


objHuman = Human()
objHuman.sayHello("Ramana")  # Here it will execute if block as name is NOT NONE
objHuman.sayHello()  # Here it will execute else block as name is NONE
print("##########################(Overloading a method - Bird)################################")

class Bird:
    def fly(self, name=None):
        if name == "parot":
            print("Parot can fly")
        if name == "penguine":
            print("Penguine cannot fly")
        if name is None:
            print("No input")


objBird = Bird()
objBird.fly()
objBird.fly("parot")
objBird.fly("penguine")
