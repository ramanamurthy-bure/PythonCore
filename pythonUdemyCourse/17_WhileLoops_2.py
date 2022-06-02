print("############# (1 - This while loop will be closed once the counter becomes 15) #############")
counter = 1
while True:
    print("Ramana")
    counter += 1

    if counter == 15:
        break
else:
    print('Hello, I am else from 1st while loop') # This will not be executed as break will exit the while loop

print("############# (2 - This while loop will be executed when the counter value is less than or equal to 10 ) ##########")

counter = 1
while counter<=10:
    counter += 1
    if counter in [4,6,8]:
        print("Ramana")
    else:
        continue
else:
    print('Hello, I am else from 2nd while loop')