#The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters
# a,p,p,l,e -> each time i will iterate into it and Print the statement
for i in "apple":
    print(i)

#range
# output -> 0,1,2,3,4 -> each time i will iterate into it and Print the statement
for i in range(5):
    print(i)

#[a,b] -> a is inclusive and b is exclusive
# 1,2,3,4 -> each time i will iterate into it and Print the statement
for i in range(1,5):
    print(i)

#Print 2 Table
for i in range(1,11):
    mul = 2*i
    print(i,"x 2 =", mul)

#
a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
c = int(input("Enter Number 3:"))
d = int(input("Enter Number 4:"))
e = int(input("Enter Number 5:"))
f = int(input("Enter Number 6:"))
g = int(input("Enter Number 7:"))
h = int(input("Enter Number 8:"))
i = int(input("Enter Number 9:"))
j = int(input("Enter Number 10:"))
sum = a+b+c+d+e+f+g+h+i+j
avg = sum/10
print(sum)
print(avg)

# it is really tough to enter all the 10 numbers.
# if it is 100 means we can't type 100 times wright. 
# 10 number means it is 10 data. so, it is collection of data,
# to store that collections we are going to use list.
# Syntax of List = [] 
# Looping Through List

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# for x in ["apple", "banana", "cherry"]
# 1st iteration -> x = apple -> it will store apple in x
# 2nd iteration -> x = banana -> it will store banana in x

#Question: Write a program to read 10 numbers from the keyboard and find their sum and avg.
#Using List Simplified Version
a = []
print("Enter The 10 Numbers")
for i in range(10):
    inp = int(input("Enter Number " + str(i+1) + ": "))
# input("Enter Number", i) -> built-in input() function in Python only accepts at most one argument, 
# but here it is two, one -> Enter Number and other -> i
# input("Enter Number" + i) -> you can't concat str and int

#CORRECT WAY:
#inp = (input("Enter Number " + str(i+1) + ": "))
#inp = int(input(f"Enter Number {i}: ")) -> using f-strings

#after getting input, need to store all the 10 entered values in somewhere, so here comes list
    a.append(inp)
print(a)

sum = 0
n = len(a)
for i in a:
    sum = sum + i
print(sum)
avg = sum/n
print(avg)

#Nested for loop
for j in range(1,3):
    print("Week: ", j)
    for i in range(1,4):
        print("Day: ", i)

#pattern question
for i in range(3):
    print("*") 
#Output->*
#        *
#        *
    
print("*", end="")
# output -> ***

print("*", end=",")
# output -> *,*,*,
#---------------------------------------

for i in range(1,5):
    print()#Gap
    for j in range(1,i+1):
        print("*", end="")

#i=1   j(1,2)->j=1
#i=2   j(1,3)->j=1,2
#i=3   j(1,4)->j=1,2,3
#i=4   j(1,5)->1,2,3,4