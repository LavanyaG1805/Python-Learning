# Dictionary {} =>
# do not allow duplicate value will overwrite existing Value
# Changeable -> Dictionaries are changeable, meaning that we can change, 
# add or remove items after the dictionary has been created.
# any type of dat can be stored 
# key:value pair ("name": "EMC")

# in value you can add str, int, list and everything
a = {
    "name" : "EMC",
    "age" : 1,
    "location" :"Tiruvannamalai",
    "Student": ["bala", "john"]
}

print(a)
print(a.keys()) # output -> only key
print(a.values()) # output -> only value
print(a.items()) # output -> key, value pair

a["age"] = 2 # you can modify the dict
a.update({"age": 2}) # you can also update the value like this

a["color"] ="red" # Adding Items
#you can add colour: red key value to the dict
print(a)

a.pop(age) #To delete it. it will delete the age key value pair
del a["age"] # this also delete it

del a # it will delete complete dic

a.clear() # it will clear all values in the dict

#Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict) #we can also use this for copy