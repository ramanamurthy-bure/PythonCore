# Approach1
import Operations

Operations.add(10, 20)  # 30
Operations.mul(2, 3)  # 6

# Approach2
from Operations import add, mul

add(40, 50)  # 90
mul(5, 6)  # 30

# Approach3
from Operations import *

add(3, 4)  # 7
mul(4, 5)  # 20
