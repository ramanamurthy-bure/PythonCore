# We will see how to access global, class and local variables when their names are same
# To access global name we need to use   globals()["variable name"]  if the same local variable name exists

a, b = 10, 50  # Global Variables


class MyClass:
    a, b = 6, 20  # Class Variables

    def add(self, a, b):  # here self means that this method is belongs to the class 'MyClass'
        print("Accessing class variables(a,b) and summing ",
              self.a + self.b)  # To access class variables we need to use self keyword
        print("Accessing local variables(c,d) and summing ", a + b)  # we can access local variables directly
        print("Accessing global variables(i,j) and summing ",
              globals()["a"] + globals()["b"])  # we can access global variables directly


obj1 = MyClass()  # Creating object in python
obj1.add(50, 20)
