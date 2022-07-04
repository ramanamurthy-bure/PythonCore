# Python Dictionaries
# Python Dictionaries are unordered mappings for string objects. Previously we saw how lists store objects
# in an ordered sequence, dictionaries use key-value pairing instead
# This key-value pair allows users to quickly grab objects without needing to know an index location
# Dictionaries use curly braces and colons to signify the keys and their associated values
# {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
# so when to choose a list and when to choose a dictionary?
# For storing the price of each item in store we can go for dictionary
# So that paccing the product name we can get the price easily
print("######################  (1) ############################################")
mydict = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print(mydict)
print("######################  (2) ############################################")
d = {'k1':123,'k2':[0,2,1,13,5],'k3':{'insidekey1': {'childkey1':1,'childkey2':2,'childkey3':3},'insidekey2':140,'insidekey3':150}}
print(d)
print(d['k2'][3]) #13
print(d['k3']['insidekey1']['childkey1']) #1
print(d['k3']['insidekey1']['childkey3']) #3
print("######################  (3) ############################################")
fruits_dict={'Apple':343,'Orange':145,'Banana':100,'Lemon':230,'Grapes':111,'Watermelon':59}
print("Before Adding new key Safota: ",fruits_dict)
fruits_dict['Safota']=223 # Adding new value to dict
print("After Adding new key Safota: ",fruits_dict)
print("Retriving Apple Price: ",fruits_dict['Apple'])
print("Retriving Watermelon Price: ",fruits_dict['Watermelon'])
fruits_dict['Watermelon']=157 # Updating existing item value
print("Retriving Watermelon Price after updating the price: ",fruits_dict['Watermelon'])
print("######################  (4) ############################################")
print("Before Poppng : ",fruits_dict)
# To pop the last item
popeditem = fruits_dict.popitem()
print("Popped Item: ",popeditem) # # It will remove the last item from the dict
print("After Applying Popitem: ",fruits_dict)
# To pop the specific item
popitem = fruits_dict.pop('Apple') # It will remove the item with the key passed from the dict
print("Pop Item: ",popitem) # To pop specific item passing the key
print("After Applying Pop for a key 'Apple'",fruits_dict)
print("######################  (5) ############################################")
# iterating the keys
print("All Keys->",end=" ")
for k in fruits_dict.keys():
    print(k,end=" ")
print("")
print("######################  (6) ############################################")
print("All Values->",end=" ")
for v in fruits_dict.values():
    print(v,end=" ")
print("")
print("######################  (7) ############################################")
print("All (Key,Value) Pairs->",end=" ")
for k,v in fruits_dict.items():
    print(k,v,end=" ")
print("")





