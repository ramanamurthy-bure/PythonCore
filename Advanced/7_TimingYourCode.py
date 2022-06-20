# As you learn more Python, you will discover multiple solutions for a single task and you may find yourself
# _ trying to figure out the most efficient approach
# An easy way to do this is to time your code's performance
# We will focus on 3 ways of doing this:
# 1. Simply tracking time elapsed
# 2. Using the timeit module
# 3. Special %%timeit "magic" for Jupyter Notebooks
print("############################# (1) #####################################")
def func_one(n):
    return [str(x) for x in range(n)]
print(func_one(10))

print("############################# (2) #####################################")
def func_two(n):
    return list(map(str,range(n)))
print(func_two(10))

print("############################# (3) #####################################")
import time
# Current time before running code
start_time = time.time()
# Run the code
result = func_one(1000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time-start_time
print(elapsed_time)

print("############################# (4) #####################################")
# Current time before running code
start_time = time.time()
# Run the code
result = func_two(1000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time-start_time
print(elapsed_time)

print("############################# (5 - timeit with function_one) #####################################")
# It's really hard to tell which function is performing better
# So we can use timeit module
import timeit
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(x) for x in range(n)]
'''
print(timeit.timeit(stmt,setup,number=100000))

print("############################# (6 - timeit with function_two) #####################################")
stmt_1 = '''
func_two(100)
'''
setup_1 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt_1,setup_1,number=100000))



