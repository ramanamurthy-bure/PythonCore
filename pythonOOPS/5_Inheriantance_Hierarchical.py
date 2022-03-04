# Hierarchical Inheritance -> Multiple childs are having one parent class
# In the below example 1 parent class P having multiple child classes OR
# Two different classes A and B are having one single parent class

class P:
    x, y = 2, 5

    def m1(self):
        print("Method m1 from class P ", self.x + self.y)


class A(P):
    a, b = 6, 8

    def m2(self):
        print("Method m2 from class A ", self.a + self.a)


class B(P):
    i, j = 10, 5

    def m3(self):
        print("Method m3 from class B ", self.i + self.j)


print("##########################(1)################################")
pobj = P()
pobj.m1()  # from class P #7
print("##########################(2)################################")
aobj = A()  # Here we can access methods from class A and class P
aobj.m1()  # from class P #7
aobj.m2()  # from class A #12
# aobj.m3()  # Invalid as m3 is belongs to class B
print("##########################(3)################################")
bobj = B()  # Here we can access methods from class B and class P
bobj.m1()  # from class P #7
# bobj.m2()  # Invalid as m2 belongs to class A
bobj.m3()  # from class B #15
