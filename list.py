# List [] =>

# Allow Duplicate 
# any type of data can be stored
# we can modify the list item. we can add or remove
# insert(), append(), extend(), pop()

a=[]
a = [1,2,3,4,5,6]
print(type(a)) # get the datatype
print(a)
a.append(7) # to add the value. it will add it in last of the list.
a.append("apple") # you can add any datatype in list 
a.append("True") # # you can add any datatype in list 
a.append(6) #you can also add duplicates to the list
print(a[1]) # to access specific element. index positing will start from 0 only
a.insert(0,11)# to add a number in a specific position
#a.insert(position[index], Value to be inserted) 
# output -> [11,1,2,3,4,5,6]
a[0] = 11 # to replace the specific index.
#output -> [11,2,3,4,5,6]
a.pop(5) # a.pop(index number) ->if you want to remove the specific index 
a.pop() # without anything it will delete the last element

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b) # if you want to merge the two list.
a.sort() # sort the list -> 1,2,3,4,5
a.sort(reverse=True)# sorting in descending order -> 5,4,3,2,1
print(a)


#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#output:['Kiwi', 'Orange', 'banana', 'cherry']
thislist.reverse() # What if you want to reverse the order of a list, regardless of the alphabet
#The reverse() method reverses the current sorting order of the elements.


#To Copy The List
mylist = thislist.copy() # Use the copy() method
mylist = list(thislist) # Use the list() method
mylist = thislist[:] # Use the slice Operator
print(mylist)

#Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
