# Class is a logical entity which contains the logic
# Class contains variable and methods
# Logic should be included with in the method

# Object is physical entity which is created for a class
# We can create any no of objects for a class
# In python function and methods are technically same but
# If a function is inside a class it is called as method

# Self is a keyword that tells the particular method belongs to the class by specifying it in method parameter
i, j = 10, 50  # Global Variables


class MyClass:
    a, b = 6, 20  # Class Variables

    def add(self, c, d):  # here self means that this method is belongs to the class 'MyClass'
        print(" It is a instance method named with 'add'")
        print("Accessing class variables(a,b) and summing ",
              self.a + self.b)  # To access class variables we need to use self keyword
        print("Accessing local variables(c,d) and summing ", c + d)  # we can access local variables directly
        print("Accessing global variables(i,j) and summing ", i + j)  # we can access global variables directly

    @staticmethod
    def mul(k, l):  # We need to use @staticmethod to make particular method as static
        print("Accessing local variables and multiplying  in static method ",
              k * l)  # static method should not have self as parameter even if it is there it will be treated as one of the parameter
        print("It is static method")

    def display(self, name):
        print("My name is ", name)
        print(" It is a instance method named with 'displaying'", name)

    def sample(self):
        pass  # When the pass statement is executed, nothing happens,
        # but you avoid getting an error when empty code is not allowed.
        # Empty code is not allowed in loops, function definitions, class definitions, or in if statements.


obj = MyClass()  # Creating object in python
obj.add(50, 20)
obj.display("Ramana")
MyClass.mul(6, 9)  # Calling static method of a class
# In python only static methods will be there NO static variables

# Creating multiple NAMED objects in python
obj1 = MyClass()  # Here object named 'obj1' will be created in the memory location for a class
obj2 = MyClass()  # Here object named 'obj2' will be created in the memory location for a class
# In the above statements both obj1 and obj2 will be created in Different memory locations
obj3 = obj1  # Here obj1 is stored in another variable named obj3
print(id(obj1))  # 2842251542144 -> id method will give the memory address of an object
print(id(obj2))  # 2842251542096 -> id method will give the memory address of an object
print(id(obj3))  # 2842251542144 -> Here same address as it is assigned directly
MyClass().display("NAMELESS object")  # -> This is a nameless object as object is not assigned to any variable

print(obj1 is obj2)  # Returns False. Here obj1 and obj2 are not same so it returns False
print(obj1 is not obj3)  # Returns False . Here obj1 and obj3 are same. Since you use 'is not' it returns False
print(obj1 is obj3)  # Returns True . Here obj1 and obj3 are same so it returns True
