employee = {}
employee['Ramana'] = {
    "address":"sdjakdjad",
    "phoneno":474374744
}
employee['Gowri'] = {
    "address":"423ddadarfsfs",
    "phoneno":55533131313
}
employee['Swamy'] = {
    "address":"ZZZZddadarfsfs",
    "phoneno":65323132
}
employee['Latha'] = {
    "address":"2323tsdadada",
    "phoneno":1111111
}
employee['Chinna'] = {
    "address":"5332eedadda",
    "phoneno":2222222
}
print(type(employee))

# Converting above dictionary to json string
import json
s = json.dumps(employee)
print(s)
print(type(s))

# Writing to a file
with open("C://Users//raman//Desktop//Ramana//Emp.txt","w") as f:
    f.write(s)


# Reading from file and
with open("C://Users//raman//Desktop//Ramana//Emp.txt", "r") as f:
    s = f.read()

print(s)
print(type(s))

empNew = json.loads(s)
print(empNew)
print(type(empNew))

print(empNew["Ramana"]["phoneno"])

for k,v in empNew.items():
    print("Key -> {} and value->{}".format(k,v))

for k in empNew:
    print(empNew[k])
