# To check which function will be called when 2 imported modules have same functions
# Here Animal and Bird have same functions fly() and color()

# Approach3 -> Here when we call fly() and color() functions it will be taken from the
# Animal module as Animal module is imported last

from Bird import *
from Animal import *


fly()  # Animal can fly
color()  # Animal is Green
