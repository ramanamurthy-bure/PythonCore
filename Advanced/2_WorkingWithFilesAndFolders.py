# 1. What if we have to open every file in a directory?
# 2. What if we want to actually move files around on our computer?
# Pythons os module and shutil allow us to easily navigate files and directories on the computer and then perform
# _ actions on them, such as moving them or deleting them.

f = open('practice.txt', 'w+')
f.write("This is a practice text")
f.close()

import os

print(os.getcwd())  # This will give current working directory
print(os.listdir())  # This will return list with all the files and folder names in the current working directory
print(os.listdir(
    "C:\\Users\\raman\\PycharmProjects"))  # This will return list with all the files and folder names in the given directory

# To check the practice.txt is present in the location
print(os.listdir("C:\\Users\\raman\\PycharmProjects\\PythonCore\\Resources"))

# The os module provides 3 methods for deleting files:
dir_path1 = "C:\\Users\\raman\\PycharmProjects\\PythonCore\\Resources\\Test"
dir_path2 = "C:\\Users\\raman\\PycharmProjects\\PythonCore\\Resources\\EmptyFolder"

if not (os.path.exists(dir_path1)):
    # To create a folder
    os.mkdir(dir_path1)
    print("Dir :" + dir_path1 + " created using os.mkdir")

if not (os.path.exists(dir_path2)):
    os.mkdir(dir_path2)
    print("Dir :" + dir_path2 + " created using os.mkdir")

import shutil

# 1. shutil.rmtree(path) -> This is the most dangerous , as it will remove all files and folders contained in the path
if os.path.exists(dir_path1):
    shutil.rmtree(dir_path1)
    print("Dir :" + dir_path1 + " removed using shutil.rmtree")

if os.path.exists(dir_path2):
    shutil.rmtree(dir_path2)
    print("Dir :" + dir_path2 + " removed using shutil.rmtree")

if not (os.path.exists(dir_path1)):
    # To create a folder
    os.mkdir(dir_path1)
    print("Dir :" + dir_path1 + " created using os.mkdir")

if not (os.path.exists(dir_path2)):
    os.mkdir(dir_path2)
    print("Dir :" + dir_path2 + " created using os.mkdir")

# To create 3 sample files for testing
for i in range(1, 4):
    f = open(str(i) + "_Sample.txt", "w+")
    f.write(str(i) + " smaple file for testing")
    print(str(i) + "_Sample.txt file got created")
    f.close()

    # To move the files for Test folder
    shutil.move(str(i) + "_Sample.txt", dir_path1)
    print(str(i) + "_Sample.txt file moved to dir: " + dir_path1)

# 2. os.unlink(path) -> Which deletes a file at the path you provided
os.unlink(dir_path1 + "\\1_Sample.txt")
print(str(i) + "_Sample.txt file deleted using os.unlink ")
os.unlink(dir_path1 + "\\2_Sample.txt")
print(str(i) + "_Sample.txt file deleted os.unlink ")

# 3. os.rmdir(path) -> which deletes a folder(folder must be empty) at the path you provided
os.rmdir(dir_path2)
print("Dir :" + dir_path2 + " removed using os.rmdir")

# _. All of these methods can not be reversed!. Which means if you make a mistake you won't be able to recover the file
# Instead we will use the send2trash module. A  safer alternative that sends deleted files to the trash bin instead
# of permanent removal.
import send2trash

send2trash.send2trash(dir_path1 + "\\3_Sample.txt")
print("3_Sample.txt file send to trash ")

# 4. shutil.rmtree(path) -> This is the most dangerous , as it will remove all files and folders contained in the path
shutil.rmtree(dir_path1)
print("Dir :" + dir_path1 + " removed using os.rmdir")
