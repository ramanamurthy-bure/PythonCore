# To check which method will be called when 2 imported modules have same methods
# Here Animal and Bird have same methods fly() and color()

# Approach1
import Animal
import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()