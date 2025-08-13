# Variables do not need to be declared with any particular type, 
# Variable Nmaes are case-sensitive. Ex: a=4, A="Sally" print(a) it will print
# You can declare string variable in singe or double quotes
"""
Legal Names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal Names:
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Muti Words Variable name:
#Camel Case -> Each word, except the first, starts with a capital letter ->Ex:myVariableName = "John"
#Pascal Case ->Each word starts with a capital letter ->Ex: MyVariableName = "John"
#Snake Case ->Each word is separated by an underscore character ->Ex: my_variable_name = "John"
#Python primarily uses snake_case for variables and function names, while PascalCase is used for class names.

a = 20
b = 20
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

a = int("10") # "10"(String) -> int("10") = 10
b = int("20")
c = a + b
print(c)

#Many Values to Multiple Variables -> Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables -> And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection -> If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)