# A is a module which contains display method in Animal class
# B is a module which contains a display method in Bird class
# So same method is there in 2 different modules

# To create objects for classes from other modules we need to used the class name while creating the object
# Like A.Animal() in the below approach

# Approach1
import A
import B
objA = A.Animal()  # Here we need to use A.Animal() to create object for Animal class which is in module A
objA.display()

objB = B.Bird()  # Here we need to use B.Bird() to create object for Bird class which is in module B
objB.display()
