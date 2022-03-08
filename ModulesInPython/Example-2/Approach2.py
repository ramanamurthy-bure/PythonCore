# To check which function will be called when 2 imported modules have same functions
# Here Animal and Bird have same functions fly() and color()

# Approach2 -> Here when we call fly() and color() functions it will be taken from the
# Bird module as Bird module is imported last

from Animal import *
from Bird import *

fly()  # Bird can fly
color()  # Bird is Green
