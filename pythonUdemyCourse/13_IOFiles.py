# Python IO Files
# Before we finish this section,let's quickly go over how to perform simple I/O with basic.txt files
# We will also discuss file paths on your computer. Let's get started.
print("######################  (1) ############################################")
file =open("C://Users//raman//PycharmProjects//pythonCore//Resources//Sample.txt","w") # open for writing
file.write("Hello this is a text file")
file.write("\nThis is a second line")
file.write("\nThis is a third line")
file.close()
print("######################  (2) ############################################")
file =open("C://Users//raman//PycharmProjects//pythonCore//Resources//Sample.txt","r") # open for reading
# When we read() the file the cursor go all the way to the end of the file.
# So we need to reset the cursor to get the text again
print("Reading for the first time :",file.read()) # This will give the all the text in one string
print("Reading again before resetting the cursor :",file.read()) # This will give empty string as the cursor is at end of the file
file.seek(0) # This will set the cursor back to the starting
print("Reading again after resetting the cursor to 0 :",file.read()) # This will give the all the text in one string
file.seek(0) # Seek back to 0
l = file.readlines()
print(l)
file.close()
# If we are opening files as above we need to close the file without miss. Else if someone was trying to access the
# file it will say Python is using the file currently
print("######################  (3) ############################################")
#using with statement
with open("/Users/raman/PycharmProjects/pythonCore/Resources/Sample.txt") as f:
    print(f.readline())
# If we use with statement, we can ignore the error mentioned in the line 21
print("######################  (4) ############################################")
# using with statement
with open("/Users/raman/PycharmProjects/pythonCore/Resources/Sample.txt",'r') as f1:
    contents = f1.read()
    print("Trying to Read Content in R mode: ", contents)
print("######################  (5) ############################################")
# using with statement
with open("/Users/raman/PycharmProjects/pythonCore/Resources/Sample.txt",'w') as f2:
    contents = f2.read() # UnsupportedOperation: not readable
    print("Trying to Read Content in W mode: ", contents)
print("######################  (6) ############################################")
# File Locations
# If we want to open files at another location on your computer,simply pass in the entire file path.
# For windows you need to use double \ so python doesn't treat the second \ as an escape character, a file
# path is in the form:
myfile = open("C://Users//raman//PycharmProjects//pythonCore//Resources//Sample.txt")
print("######################  (7) ############################################")
# For MacOS and Linux you use slashes in the opposite direction:
myfile = open("/Users/raman/PycharmProjects/pythonCore/Resources/Sample.txt")
print("######################  (8) ############################################")
# Reading modes:
# 'r' : For read only
# 'w' : For write only(Will overwrite files or create new!)
# 'a' : For append only (Will add on to files)
# 'r+' : For reading and writing
# 'w+' : For reading and writing(Will overwrites existing files or creates a new file!)













