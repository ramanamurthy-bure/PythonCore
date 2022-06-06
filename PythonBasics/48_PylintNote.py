# As you begin to expand to large multi-file projects it becomes important to have tests in place
# This way as you make changes or update your code, you can run your test files to make sure
# previous code still runs as expected
# There are several testing tools, we will focus on two,
# 1.pylint : This is a library that looks at your code and reports back possible issues
# 2.unittest : This built-in library will allow to test your own programs and check you are getting desired output
# We will begin by showing you how to use pylint to check your code for possible errors and styling
# Python as set of style convention rules known as 'PEP 8'
# Afterwords we will explore how to test our code with the built-in unittest library
'''
A Very simple code to check pylint report
'''
# To check the syntax errors and to report possible issues,
# we can navigate to the same directory where this .py is placed and then
# type the command 'pylint 48_PylintTest.py -r y'
# type the command 'pylint pylint_test -r y'
# pylint_test is designed to meet good coverage.
a=1
b=2
print(a)
print(B)
