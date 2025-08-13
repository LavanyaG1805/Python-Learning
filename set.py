# set {} =>
# Do not allow duplicate, duplicate values are removed
# any type of data can be stored
# we cannot modify the set item but we can add or remove items.
# sets are unordered.
# add(), update(), remove(), pop()

a={}
a={1,2,3,4,1}
print(a) #output -> {1,2,3,4}
#print(a[1])
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, 
# or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  

a[0] = 10 # we can't modify the set but we can add and remove item
a.add(10) # output -> [1,2,3,4,10]
a.remove(2) # output -> [1,3,4,10] 
# you can use remove and discard to remove particular element

a.pop() #it should remove last element but it is removing first becoz it is unordered
# the order will change everytime when you run it.
a.clear()#clear() method empties the set
del a #del keyword will delete the set completely


#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

