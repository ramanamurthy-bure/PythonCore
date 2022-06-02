class DogClass():
    def __init__(self,breed,name,spots): # This is a constructor for the class. It is going to be called
        # automatically when you create instance of the class

        # self is the reference to the instance of the class

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name

        self.breed = breed
        self.name = name

        # Expecting boolean True/False
        self.spots = spots

# creating instance of DogClass
# my_dog = DogClass() # Not Valid, 1 positional arg is required
# my_dog = DogClass("Lab") # Valid

my_dog = DogClass(breed = "Lab",name='Samyy',spots=True)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)




