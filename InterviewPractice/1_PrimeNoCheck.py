n1 = int(input("Start #: "))
n2 = int(input("End #: "))

if n1<=2 or n2<=2:
    for i in range(n1,n2):
        flag = False
        for j in range(2,int(i/2)+1):
            if(i%j == 0):
                flag = True
        if not flag :
            print(i)
else:
    print("No should be greater than 2")
