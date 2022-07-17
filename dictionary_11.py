#DICTIONARY

a = {1:'ragosh',2:'shrestha',3:'python','program':4}
#here left side is a key and the right side is the dictionary value

#ACCESS
print(a[3])
"""It searches the desired value using the key"""

#LENGTH -> counts the number of key value
print(len(a))

#CLEAR
print(a.clear())

#COPY -> it is used to copy the item inside the dictionary
b = a.copy()
print(b)

#GET  -> it returns a value for a given key
a = {1:'ragosh',2:'shrestha',3:'python','program':4}
print(a.get(2))

#ITEMS -> it returns list of dict having key in tuple form
print(a.items())

#KEYS -> it returns the list of key inside the dictionary
print(a.keys())

#UPDATE -> it is used to add two or more dictionary in one single
a = {1:'ragosh',2:'shrestha',3:'python','program':4}
b = {4:'hiii',5:'helo',6:'fun','code':4}
a.update(b)
print(a)

#VALUES -> it returns all the values present in the dictionary
print(a.values())

a = {1:'ragosh',2:'shrestha',3:'python','program':4}
a[5]='cool' #here a[5] is not a array with index 5, It is a dict with key = 5
print(a)

a = {1:'ragosh',2:'shrestha',3:'python','program':4}
del a[3]
print(a)
