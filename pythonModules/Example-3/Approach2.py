# A is a module which contains display method in Animal class
# B is a module which contains a display method in Bird class
# So same method is there in 2 different modules

# To create objects for classes from other modules we need to used the class name while creating the object
# Like A.Animal() in the below approach

# Approach2
from A import Animal
from B import Bird
objA = Animal()  # Here we no need to
