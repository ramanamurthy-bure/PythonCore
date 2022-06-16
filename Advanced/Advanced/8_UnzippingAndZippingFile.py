import os.path
import shutil
folder_path = "C:\\Users\\raman\\PycharmProjects\\PythonCore\\Advanced\\Advanced"
print("############################### Cleaning the files ################################################")
# To remove the folder extracted_contenent
if os.path.exists(folder_path+"\\extracted_contenent"):
    shutil.rmtree(folder_path+"\\extracted_contenent")
    print("Removed folder "+folder_path+"\\extracted_contenent")

# To remove the folder final_zip
if os.path.exists(folder_path+"\\final_zip"):
    shutil.rmtree(folder_path+"\\final_zip")
    print("Removed folder " + folder_path + "\\final_zip")

# To remove the folder comp_file.zip
if os.path.exists(folder_path+"\\comp_file.zip"):
    os.unlink(folder_path+"\\comp_file.zip")
    print("Removed zip file " + folder_path + "\\comp_file.zip")

# To remove the folder example.zip
if os.path.exists(folder_path+"\\example.zip"):
    os.unlink(folder_path+"\\example.zip")
    print("Removed zip file " + folder_path + "\\example.zip")

# To remove the 4 text files before creating them for test
for i in range(1, 5):
    file_path = folder_path + "\\Test_" + str(i) + ".txt"
    if os.path.exists(file_path):
        os.unlink(file_path)
        print("Removed text file " + file_path)

print("############################### Creating the files ################################################")
# Creating 4 text files for zipping it later
for i in range(1,5):
    f=open("Test_"+str(i)+".txt","w+")
    f.write("This is sample text : "+str(i))
    if i == 3:
        f.write("\n My phone no is : 333-563-6674")
    print("Created text file: " + "Test_"+str(i)+".txt")
    f.close()

import zipfile

# Creating Zip  file and writing sample text files created above
comp_file = zipfile.ZipFile('comp_file.zip','w') # This will create empty zip file named comp_file.zip
comp_file.write('Test_1.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Test_2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Test_3.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Test_4.txt',compress_type=zipfile.ZIP_DEFLATED)
print("Created comp_file.zip and compressed all the 4t text files created above")
comp_file.close()

# Extracting Zip files
zip_obj = zipfile.ZipFile('comp_file.zip','r')# This will create zip_obj for extracting the files
zip_obj.extractall('extracted_contenent') # This will extract all the files from comp_file to new folder named extracted_contenent
print("Extracted the 'comp_file.zip' file to new folder 'extracted_contenent'")

import shutil
# Now converting the extracted_content folder to example.zip file
dir_to_zip = folder_path+"\\extracted_contenent"
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)
print("Compressed the folder 'extracted_contenent' to 'example.zip' file")

# Now converting the example.zip to folder with extracted content
shutil.unpack_archive('example.zip','final_zip','zip')
print("Extraced the file 'example.zip' to 'final_zip' folder")
