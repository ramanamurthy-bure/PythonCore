# In this section we will explore how to send e-mails with Python and how to check our inbox for
# received messages. Please keep in mind this process is highly reliant on admin privileges on
# both your local computer, you internet, and your email.

# It is highly likely that on a corporate network, work computer, or work email these methods
# will be blocked for security reasons
# If you encounter issues due to this , please contact your IT department,
# as it is not an issue we can fix on our end

# Each major e-mail provider has their own SMTP(Simple Mail Transfer Protocol) server.

# Provider                          SMTP server domain name
# Gmail(Will need app password)     smtp.gmail.com
# Yahoo Mail                        smtp.mail.yahoo.com
# Outlook.com/Hotmail.com           smtp-mail.outlook.com


# Sending e-mails with Python
# We will go over this process with a Gmail account
# For gmail users , you will need to generate an app password instead of your normal password
# This let's Gmail know that the Python script attempting to access your account is authorized by you

# Overview of Sending Emails
# The smtplib library allows you to manually go through the steps of creating and sending an email in Python:

#Create an SMTP object for a server. Here are the main Server Domain Name for the top email services.
#If you don't see your email server here, you may need to do a quick Google Search to see if there SMTP server domain name is available:
#Provider	                            SMTP server domain name
#Gmail (will need App Password)	        smtp.gmail.com
#Yahoo Mail	                            smtp.mail.yahoo.com
#Outlook.com/Hotmail.com	            smtp-mail.outlook.com
#AT&T	                                smpt.mail.att.net (Use port 465)
#Verizon	                            smtp.verizon.net (Use port 465)
#Comcast	                            smtp.comcast.net

import smtplib
#Next is to create an STMP object that can make the method calls to log you in to your email in order to
#send messages. Notice how also specify a port number. If the number 587 does not work on your computer,
#try using 465 instead. Keep in mind, a firewall or antivirus may prevent Python from opening up this port,
#so you may need to disable it on your computer.
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo() # This is required to start the server

#Next we run the ehlo() command which "greets" the server and establishes the connection.
#This method call should be done directly after creating the object. Calling it after other methods may result
#in errors in connecting later on. The first item in the tuple that is returned should be 250,
#indicating a successful connection.

# print(smtp_obj.ehlo())

# Now its time to set up the email and the passwords. You should never save the raw string of your
# password or email in a script, because anyone that sees this script will then be able to see you email
# and password! Instead you should use input() to get that information. If you also don't want your password
# to be visible when typing it in, you can use the built-in getpass library that will hide your password as
# you type it in, either with asterisks or by just keeping it invisible.

smtp_obj.starttls()

# Note for Gmail Users, you need to generate an app password instead of your normal email password.
# This also requires enabling 2-step authentication. Follow the instructions here to set-up 2-Step Factor
# Authentication as well as App Password Generation:https://support.google.com/accounts/answer/185833?hl=en/.
# Set-up 2 Factor Authentication, then create the App Password, choose Mail as the App and give it any name you
# want. This will output a 16 letter password for you. Pass in this password as your login password for the smtp.

import getpass
email = getpass.getpass("Enter your email: ")
# This is the app password
password = getpass.getpass("Enter your password: ")

#qlprwckfxyqohmxo
smtp_obj.login(email,password)

# Now we can send an email using the .sendmail() method.
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_obj.sendmail(from_address,to_address,msg)
# {}
# If you get back an empty dictionary, then the sending was successful.
# You can then close your session with the .quit() method.

smtp_obj.quit()

