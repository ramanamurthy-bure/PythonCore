'''
PDFs and Spreadsheets Puzzle Exercise
Let's test your skills, the files needed for this puzzle exercise

You will need to work with two files for this exercise and solve the following tasks:

Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal
 from top left to bottom right).
Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you
 can't download from Google Drive) and find the phone number that is in the document.
 Note: There are different ways of formatting a phone number!

'''

# Task One: Grab the Google Drive Link from .csv File
import csv
# Grab all the lines of data.

data = open('Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
# We can see its along the diagonal, which means the values are at the index position that matches the
# row's number order. So the 1st letter is the 1st item in the 1st row, the 2nd letter is the 2nd item in
# the 2nd row, the 3rd item is the 3rd letter in the 3rd row and so on. We can use enumerate to track the
# row number and simply index off the data_lines.

# Method One

link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
''.join(link_list) # 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'


# Method Two

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
print(link_str) # 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'

# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
# You should get this phone number
# 505 503 4455
import PyPDF2
f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
print(pdf.numPages)

# Phone Number Matching
# Lot's of ways to do this, but you had to figure out the phone number was in format ###.###.####

# Hint: https: // stackoverflow.com / questions / 4697882 / how - can - i - find - all - matches - to - a - regular - expression - in -python

import re

pattern = r'\d{3}'
all_text = ''

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text
for match in re.finditer(pattern, all_text):
    print(match)

#Once you know the correct pattern:

import re

pattern = r'\d{3}.\d{3}.\d{4}'
for n in range(pdf.numPages):

    page = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern, page_text)

    if match:
        print(match.group()) # 505.503.4455

