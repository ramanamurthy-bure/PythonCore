# Polymorphism
# Refers the way in which different object classes can share the same name

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + 'says woof!'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + 'says meow!'


niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

print("########### (Iterating different class instances) #################")
for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(type(pet.speak()))
    print("############################")


# Creating the function with class object instance as a parameter
def pet_speak(pet):
    print(pet.speak())


# Here based on the instance passed the speak method will be called
pet_speak(niko)
pet_speak(felix)
