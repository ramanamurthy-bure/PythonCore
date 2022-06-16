# You should see 5 folders , each with a lot of random.txt files. Within one of these text files is a
# _ telephone number formatted ###-###-####. Use the Python os module and regular expression to iterate through
# _ each file, open it, and search for a telephone number

import os
dir_path = "C:\\Users\\raman\\PycharmProjects\\PythonCore\\Advanced\\Advanced\\extracted_contenent"


def find_phoneno(mytext):
    import re
    text_pattern = r'(\d{3})-(\d{3})-(\d{4})'
    result = re.search(text_pattern, mytext)
    if result != None:
        return result.group()
    else:
        return "Not Found"

for folder,subfolders,files in os.walk(dir_path):
    print(f'Currently looking at {folder}')
    print('\n')
    print('The sub folders are')
    for subfolder in subfolders:
        print(f"Sub folder: {subfolder}")
    print('\n')
    print('The Files')
    for file in files:
        with open(file,'r') as f:
            text = f.read()
            print("File Text : "+text)
            print("Phone no : "+find_phoneno(text))

