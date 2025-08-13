# Tupple () =>
# Allows Duplicate
# Any type of data can be stored
# we cannot modify the tuple item. we cannot add or remove.

a=()
a =(1,2,3,4)
print(a)
print(a[2])#To access the element
# use negative indexing to print last item of tuple. a[-1]


#a[0] = 10 -> we can't modify tuple item
b = list(a) #but we can do casting and convert that to list
print(type(a)) #tuple
print(type(b)) #list
# after converting to list we can modify it
b.pop()
b[0] = 10
a = tuple(b) #again converted back to the own format

#delete the tuple
del(a)


#join Tuple:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Count Tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
# Return the number of times the value 5 appears in the tuple
# Output - 2

# Index Tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
# Output - 3



