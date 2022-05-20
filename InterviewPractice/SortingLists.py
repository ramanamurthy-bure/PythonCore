l = [2, 5, 1, 10, 4, 8, 32, 34, 90]
print("Before Sorting -> "+str(l))
l.sort(reverse=True)
print("After Sorting with Reverse as True -> "+str(l))
l.sort(reverse=False)
print("After Sorting with Reverse as False -> "+str(l))
l.sort()
print("After Sorting with Reverse as False- Default sorting-Ascending Order -> "+str(l))
