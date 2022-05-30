# Formating Output
# using format methods
print("######################  (1) ############################################")
name = "Ramana"
print("This is a strnig {} ".format('Inserted')) #This is a strnig Inserted
print("This is a {} {} strnig {} ".format('Inserted',"XX","YY")) #This is a Inserted XX strnig YY
print("This is a {c} {a} strnig {b} ".format(a='Inserted',b="XX",c="YY")) #This is a YY Inserted strnig XX
print("This is a {2} {0} strnig {1} ".format('Inserted',"XX","YY")) #This is a YY Inserted strnig XX
print("This is a {0} {0} strnig {0} ".format('Inserted',"XX","YY")) #This is a Inserted Inserted strnig Inserted
print("######################  (2) ############################################")
# Float Formating Follow as
# {value:width.precision f}
# Value - Value variable
# Width - For space
# Precision - For no of decimal points
result = 100/777
print("The results was: {} ".format(result)) #The results was: 0.1287001287001287
print("The results was: {r} ".format(r=result)) #The results was: 0.1287001287001287
print("The results was: {r:1.3f}".format(r=result)) #The results was: 0.129
print("The results was: {r:10.3f}".format(r=result)) #The results was:      0.129
print("The results was: {r:1.2f}".format(r=result)) #The results was: 0.13
print("The results was: {r:1f}".format(r=result)) #The results was: 0.128700
print("######################  (3) ############################################")
# using fString methods
name = "Ramana"
print("My name is : {} ".format(name)) #My name is : Ramana
print(f"My name is : {name} ") #My name is : Ramana
print("######################  (4) ############################################")
name = "Ramana"
age = "35"
Sal = "30"
print(f"Name: {name} Age: {age} Sal: {Sal}")




