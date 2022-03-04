# Classes can inherit the functionalities of other classes
# If an object is created using a class that inherits from a superclass,
# the object will contain the methods and variables of both class, it's superclass.

# The parent class can be called as Base Class or Super Class
# The child class can be called as subclass or derived class

# Types of inheritance - total 5 types
# 1. Single -> One parent and one child class
# 2. Multi Level -> One parent and one child and this child in turn will have one more child etc...
# 3. Hierarchical -> Multiple childs are having one parent class
# 4. Multiple -> One child having multiple parents
# 5. Hybrid -> Combination of both hierarchical and multiple is called hybrid inheritance

class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):  # Single Inheritance
    def m2(self):
        print("This is m2 method from class B")


print("##########################(1)################################")
aobj = A()
aobj.m1()  # Here we can call only m1 method present in the class A
print("############################(2)##############################")
bobj = B()  # Here we can call only m1 method present in the class A and m2 from class B.
bobj.m1()  # from class A -> It is allowed as class B inherited from class A
bobj.m2()  # from class B
