# Multi level inheritance -> One parent and one child and this child in turn will have one more child etc...
class A:
    x, y = 89, 13

    def m1(self):
        print("Method m1 from class A ", self.x + self.y)


class B(A):  # Single Inheritance
    a, b = 54, 67

    def m2(self):
        print("Method m2 from class B ", self.a + self.a)


class C(B):  # Multi Level Inheritance
    i, j = 55, 52

    def m3(self):
        print("Method m3 from class C ", self.i + self.j)


print("##########################(1)################################")
bobj = B()  # Here with this bobj we can access methods from class B and Class A
bobj.m1()  # from class A
bobj.m2()  # from class B
print("##########################(2)################################")
cobj = C()  # Here with this cobj we can access methods from class C, Class B and class A
cobj.m1()  # from class A
cobj.m2()  # from class B
cobj.m3()  # from class C
