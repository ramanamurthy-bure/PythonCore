#Overview of Received Emails
# Now that we understand how to send emails progammatically with Python, let's explore how
# we can read and search recieved emails. To do we will use the built-in imaplib library.
# We will also use the built in email library for parsing through the recieved emails.

import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
user = input("Enter your email: ")
# Remember , you may need an app password if you are a gmail user
#
password = getpass.getpass("Enter your password: ")

M.login(user,password)

M.list()

# Connect to your inbox
M.select("inbox")

# Searching Mail
# Now that we have connected to our mail, we should be able to search for it using the specialized
# syntax of IMAP. Here are the different search keys you can use:
# We can refer the search.html file for the same

# You can also use the logical operators AND and OR to combine the above statements. Check out the
# full list of search keys here: http://www.4d.com/docs/CMU/CMU88864.HTM.

# Please note that some IMAP server providers for different email services will have slightly different syntax.
# You may need to experiment to get the results you want.

#Now we can search our mail for any term we want.

# Use if you get an error saying limit was reached
imaplib._MAXLINE = 10000000

#Send yourself a test email with the subject line:

# this is a test email for python

# Or some other uniquely identifying string.

# We will now need to reconnect to our imap server. You will probably need to restart your kernel
# for this step if you are using jupyter notebook.

# Restart your kernel and run the following:
import imaplib
import getpass
M = imaplib.IMAP4_SSL('imap.gmail.com')
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)

# Connect to your inbox
M.select("inbox")

#Let's now search and confirm if it is there:
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')
#We can now save what it has returned:

# typ, data = M.fetch(data[0],"(RFC822)")
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# We can use the built in email library to help parse this raw string.

import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)


# b'This is a test to see if the python search worked.\r\n'
# Excellent! We've successfully have been able to check our email's inbox ,
# filter by some condition, and read the body of the text that was there.
# This will come in handy in the near future!