# Problem-1
# Handle the exception thrown by the below code using try and except blocks

def tryexcepttest():
    print('########################### (Prob - 1) ######################################')
    while True:
        try:
            for i in [1, 2, 3,5, 'a']:
                print(i ** 2)
                if i == 5:
                    i % 0
        except ArithmeticError:
            print("Caught Arithmetic Error")
        except:
            print("Caught TypeError")
        else:
            print("All the inputs accepted!")
        finally:
            print("All Done!")
            break

# Problem-2
# Write a function that asks for an integer and prints the square of it. Use a while loop
# with a try,except, else block to acount incorrect inputs

def ask():
    while True:
        print('########################### (Prob - 2) ######################################')
        try:
            n = int(input("Enter integer no: "))
        except:
            print("Enter valid input no ")
            continue
        else:
            break

if __name__ == "__main__":
    ask()