# Special Methods
print("######################### (1) #################################")
my_list = [1, 2, 3]
print(len(my_list))  # 3
print(my_list)  # [1, 2, 3]


class Sample():
    pass


mysample = Sample()
# print(len(mysample)) # TypeError: object of type 'Sample' has no len()
print(mysample)  # <__main__.Sample object at 0x0000029DE8F87C40>

print("######################### (2) #################################")


# We will see how we can use same built in python functions with my own user defined objects using specila methods
# We call them as Magic or Dunder methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book('Python Rocks', 'Jose', 200)
# print(b) # This will give string representation of the book class
# print(str(b)) # This will give string representation of the book class
# Now using the special method __str__ we can override this representation and write our own code(like in Line #24)
print(b)
print(len(b))
del b  # This will print the message in line # 31
