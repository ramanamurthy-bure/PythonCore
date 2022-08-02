d = {'k1': 1, 'k2': 2}
s1 = {x: x ** 2 for x in range(5)}
print(s1)

s2 = {k: v ** 2 for k, v in zip(['a', 'b', 'c'], range(1, 3))}
print(s2)
