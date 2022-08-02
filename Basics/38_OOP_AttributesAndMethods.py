class Circle():
    # Class object Attribute
    pi = 3.14

    # this class attributes can be called using the self keyword or the name of the class
    # example: self.pi or Circle.pi

    # Constructor
    def __init__(self, radius=1):
        self.radius = radius
        self.area = self.pi * radius * radius
        self.area = Circle.pi * radius * radius  # Valid

    # Method
    def get_circumfrence(self):
        return self.radius * self.pi * 2


print("#################### (1) #############################")
# creating instance of a class
my_circle = Circle()  # Valid as radius is default parameter
# calling the attribute
print("Pi: ", my_circle.pi)  # 3.14
print("Radius: ", my_circle.radius)  # 1
print("Area:", my_circle.area)  # 3.14

# calling the method
print("Circumfrence: ", my_circle.get_circumfrence())  # 6.28

print("#################### (2) #############################")
# creating instance of a class
my_circle1 = Circle(2)  # Valid as radius is default parameter
# calling the attribute
print("Pi:", my_circle1.pi)  # 3.14
print("Radius:", my_circle1.radius)  # 2, which is passed while creating the class instance in line 24
print("Area:", my_circle1.area)  # 12.56

# calling the method
print("Circumfrence:", my_circle1.get_circumfrence())  # 12.56
