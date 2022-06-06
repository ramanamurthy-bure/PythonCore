# Multiple -> One child having multiple parents
# In this below example class C inherited from two different classes A and B

class A:
    x, y = 6, 9

    def m1(self):
        print("Method m1 from class A ", self.x + self.y)


class B:
    a, b = 16, 28

    def m2(self):
        print("Method m2 from class B ", self.a + self.a)


class C(A, B):  # Multiple Inheritance. Here C inherited from 2 different classes. one child class inherited 2 diff parent classes
    i, j = 20, 45

    def m3(self):
        print("Method m3 from class C ", self.i + self.j)


print("##########################(1)################################")
cobj = C()  # Here we can access methods m1,m2,m3 from this object cobj
cobj.m1()  # from class A # 15
cobj.m2()  # from class B # 32
cobj.m3()  # from class C # 65
