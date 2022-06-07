import math
# print(help(math))
print("################################ (1 - math) ######################################")
value = 4.35
print(math.floor(value)) #4
print(math.ceil(value)) #5
print(round(value)) #4
# IF the value passing to the round function is .5 then it will return the even no always
print(round(4.5)) #4 - It will always returns the even no. So it will return 4 itself as it is even
print(round(5.5)) #6 - It will alwyas returns the even no so it will give the next no as 6 is even instead of 5
print(round(2.5)) #2 - It will always returns the even no. So it will return 2 itself as it is even
print(round(3.5)) #4 - It will always returns the even no so it will give the next no as 4 is even instead of 3
print(round(2.7)) #3
print(round(3.7)) #4

print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.inf) #inf
print(math.nan) #nan
print(math.log(math.e)) #1.0
print(math.log(100,10)) #2.0
print(math.log(4,2)) #2.0
print(math.sin(10)) #-0.5440211108893698
print(math.degrees(math.pi/2)) #90.0
print(math.radians(180)) #3.141592653589793
print("################################ (2 - random) ######################################")

import random
print(random.randint(0,100))

random.seed(101)
print(random.randint(0,100)) # This will give 74 always as we applied seed above
print(random.randint(0,100)) # This will give 24 always as we applied seed above
print(random.randint(0,100)) # This will give 69 always as we applied seed above

print("################################ (3 - taking 1 random no from list) ######################################")
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist)) #11
print(random.choice(mylist)) #14

print("################################ (4 - taking 5 random nos from list) ######################################")
mylist = list(range(0,20))
print(mylist)
# Sample with replacement
print(random.choices(population=mylist,k=10)) # Here same no can be picked twice

# Sample without replacement
print(random.sample(population=mylist,k=10)) # Here the picked no are unique

print("################################ (5 - shuffling the list) ######################################")
mylist = list(range(0,20))
print(mylist)
random.shuffle(mylist)
print(mylist) # Here the origional list is effected

print("################################ (6 - random floring point nos ) ######################################")
print(random.uniform(a=0,b=100)) #74.44690143237648

print(random.gauss(mu=0,sigma=1)) #-1.7665992795896235




