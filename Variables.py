# Variables do not need to be declared with any particular type, 
a = 10 
b = 10
c = a + b
print(c)

#To get the datatype of the variable
a = 10
print (type(a))

b = "ball"
print(type(b))

#Casting = converting one data type to other data type
a = "10"
b = "20"
c = a + b
print(c)
#Output = 10 ->string + 20 ->string = 1020 -> both are string so it concating this.

a = int("10") # Casting -> it is converted from string to int 
b = int("20")
c = a + b
print(c)