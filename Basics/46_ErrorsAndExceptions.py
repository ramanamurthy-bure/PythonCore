# Errors are bound to happen in your code
# Especially when someone else ends up using it in an unexpected way
# We can use error handling to attempt to plan for possible errors
# For example : a user may try to write to a file that was only opened in mode='r'
# Currently if there is any type of error in your code, the entire script will stop
# We can use Error Handling to let the script continue with other code, even if there is an error

# We use 3 keywords for this:
# try : This is the block of code to be attempted (May lead to an error)
# except : Block of code will execute in case there is an error in try block
# finally : A final block of code to be executed, regardless of an error

print('########################### (1) ######################################')
try:
    f = open('testfile', 'w')
    f.write("Write a test line to the file")
except TypeError:
    print("I will run when there is Type error!")
except OSError:
    print("I will run when there is OS error!")
except:
    print("This is for all other exceptions(other than TypeError and OSError")
finally:
    print('I always run')

print('############################# (2) ####################################')
while True:
    try:
        result = int(input('Please provide number: '))
    except:
        print("Whoops! That is not a number")
        continue
    else:
        print("yes thanks you")
        break
    finally:
        print("End of try/except/finally")
        print("I will always run at the end!")
