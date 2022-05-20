# While working with Binary search all the values need to be sorted first
pos = -1
def findTheElemnt(l1,n):
    l1 = sorted(l1)
    print("List->",l1)
    print("Target->",n)
    l= 0
    print("Lower: ", l)
    u = len(l1)-1
    print("Upper: ", u)

    while l <= u:
        mid = (l+u)//2
        print("Mid : ",mid)

        if l1[mid] == n:
            # print("Found")
            globals()['pos'] = mid
            return True
        else:
            if l1[mid] < n:
                l = mid+1
                print("Lower: ", l)
            else:
                u = mid-1
                print("Upper: ", u)
    return False


l1 = [1, 2, 3, 3, 5, 6, 34, 67, 90, 321, 453, 656]
n = 6

if findTheElemnt(l1,n):
    print("Found at index: ",pos)
else:
    print("Not Found")



