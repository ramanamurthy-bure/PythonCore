class DogClass():
    # Class Object Attributes.
    # These are same for any instance of the class
    # Here no need to use self keyword as these are same for all the instances
    species = 'Mammal'

    def __init__(self, breed, name, spots):  # This is a constructor for the class. It is going to be called
        # automatically when you create instance of the class

        # self is the reference to the instance of the class

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name

        self.breed = breed
        self.name = name

        # Expecting boolean True/False
        self.spots = spots

    # creating class methods
    # Operations/Actions can be done using the methods
    # Methods will look similar to functions. It is called methon when it is defined in the class
    def bark(self, number):
        print("Woof, My name is {} and the number is {} ".format(self.name, number))
        # Here for accessing the class variable we need to use self keyword,
        # number is local variable to the method bark


# creating instance of DogClass
# my_dog = DogClass() # Not Valid, 1 positional arg is required
# my_dog = DogClass("Lab") # Valid

my_dog = DogClass(breed="Lab", name='Samyy', spots=True)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
# When calling the attributes, we will not use the parenthesis like above
# For calling the class methods we need to give the parenthesis like below
my_dog.bark(2)
