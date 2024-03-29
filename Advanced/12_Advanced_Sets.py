s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)

# To clear the set
s.clear()
print(s)

# To copy the set
s = {1, 2, 3}
print(s)
sc = s.copy()
print(sc)
sc.add(4)
print(sc)

# To find the difference between 2 sets
print(s.difference(sc))  # set()
print(sc.difference(s))  # {4}

s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)  # {2,3}

s = {1, 2, 3, 4}
print(s)  # {1, 2, 3, 4}
s.discard(2)
print(s)  # {1, 3, 4}

s1 = {1, 2, 3, 4}
s2 = {2, 4, 5}
print(s1.intersection(s2))  # {2,4}
s1.intersection_update(s2)
print(s1)  # {2,4}

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s2))  # False
print(s1.isdisjoint(s3))  # True
print(s1.issubset(s2))  # True
print(s1.issubset(s3))  # False
print(s1.symmetric_difference(s2))  # {4}
print(s1.union(s2))
