# Object Oriendted Programming : OOP
# Allows programmers to create their own objects that have methods and attributes
# Recall that after defining a string , list, dictionary, or other objects, you were able to call methods off
# of them with .method_name() syntax
# Class name follows camel casing-where every individual word has first letter in caps
# __init__ method within class allows to create instance of the class
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)

# Example Class Below
class Sample():
    pass

# creating instance of the above class
my_sample = Sample()

print(type(my_sample))
