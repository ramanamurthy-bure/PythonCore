'''

Working with CSV Files
Welcome back! Let's discuss how to work with CSV files in Python. A file with the CSV file extension is a
Comma Separated Values file. All CSV files are plain text, contain alphanumeric characters, and structure
the data contained within them in a tabular form. Don't confuse Excel Files with csv files, while csv files
are formatted very similarly to excel files, they don't have data types for their values, they are all strings
with no font or color. They also don't have worksheets the way an excel file does. Python does have several
libraries for working with Excel files, you can check them out here and here.

Files in the CSV format are generally used to exchange data, usually when there's a large amount, between
different applications. Database programs, analytical software, and other applications that store massive
amounts of information (like contacts and customer data), will usually support the CSV format.

Let's explore how we can open a csv file with Python's built-in csv library.

Notebook Location.
Run pwd inside a notebook cell to find out where your notebook is located

print(pwd)
'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets'

'''

# Reading CSV Files
import csv

# When passing in the file path, make sure to include the extension if it has one,
# you should be able to Tab Autocomplete the file name. If you can't Tab autocomplete,
# that is a good indicator your file is not in the same location as your notebook.
# You can always type in the entire file path (it will look similar in formatting to the output of pwd.

data = open('example.csv')
print(data)

# Encoding
# Often csv files may contain characters that you can't interpret with standard python, this could be
# something like an @ symbol, or even foreign characters. Let's view an example of this sort of error
# (its pretty common, so its important to go over).

# csv_data = csv.reader(data)
# data_lines = list(csv_data)
# print(data_lines)

# Cast to a list will give an error, note the can't decode line in the error, this is a giveaway that
# we have an encoding problem!
# Let's not try reading it with a "utf-8" encoding.

data = open('example.csv', encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
# Looks like it worked!

data_lines[:3]
# Note the first item in the list is the header line, this contains the information about what
# each column represents. Let's format our printing just a bit:

for line in data_lines[:5]:
    print(line)

# Let's imagine we wanted a list of all the emails. For demonstration, since there are 1000 items
# plus the header, we will only do a few rows.
print(len(data_lines))

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

# ['jzaniolini0@simplemachines.org', 'fdrillingcourt1@umich.edu', 'nherity2@statcounter.com',
# 'ofrayling3@economist.com', 'jmurrison4@cbslocal.com', 'lgamet5@list-manage.com', 'dhowatt6@amazon.com',
# 'kherion7@amazon.com', 'chedworth8@china.com.cn', 'hgasquoine9@google.ru', 'ftarra@shareasale.com',
# 'abathb@umn.edu', 'lchastangc@goo.gl', 'cceried@yale.edu']

# What if we wanted a list of full names?
full_names = []

for line in data_lines[1:15]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names)

# Writing to CSV Files
# We can also write csv files, either new ones or add on to existing ones.

# New File
# This will also overwrite any exisiting file with the same name, so be careful with this!

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'.
file_to_output = open('to_save_file.csv', 'w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()

# Existing File
f = open('to_save_file.csv', 'a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new', 'new', 'new'])
#13
f.close()
# That is all for the basics! If you believe you will be working with CSV files often,
# you may want to check out the powerful pandas library.
