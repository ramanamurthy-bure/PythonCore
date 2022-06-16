from abc import abstractmethod, ABC


class X(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class Y(X):
    def m1(self):
        print("Implementation for abstract method m1 from abstract class X")


# objy = Y()
# objy.m1()  # We will get error : Can't instantiate abstract class Y with abstract method m2.
# As m2 is not implemented in class Y yet.
# Until we implement all the abstract methods, it will not allow object creation


class Z(Y):
    def m2(self):
        print("Implementation for abstract method m2 from abstract class X")


objz = Z()
objz.m1()  # Here we will not get any error as the both the methods are implemented.
# m1 implemented in class Y and m2 implemented in class Z. As class Z extends class Y.
# So it will allow crating object

