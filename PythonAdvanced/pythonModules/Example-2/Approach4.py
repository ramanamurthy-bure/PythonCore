# To check which function will be called when 2 imported modules have same functions
# Here Animal and Bird have same functions fly() and color()

# Approach4 -> When multiple modules are having same functions we can use
# below approach to solve the conflict from approach 2 and 3

from Bird import *
fly()  # Bird can fly
color()  # Bird is Green

from Animal import *
fly()  # Animal can fly
color()  # Animal is Green

# In this approach we are importing the modules in between so in line 8 & 9 it will use functions from Bird module
# In this approach we are importing the modules in between so in line 12 & 13 it will use functions from Animal module
