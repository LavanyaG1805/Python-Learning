#Question-1
a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
#a=9, b=1
for i in range(a,b):
    if(a>b):
        print(i)
    else: 
        print()

#Question-2 Print Even Numbers
for i in range(1,11):
    if(i%2==0):
        print(i)

#Question-3 Count Event Numbers
count = 0
for i in range(1,11):
    if(i%2==0):
        count = count + 1
print(count)

#Question-4 Count Even and Odd numbers
Ecount= 0
Ocount = 0
for i in range(1,11):
    if(i%2==0):
        Ecount = Ecount + 1
    else:
        Ocount = Ocount + 1
print("Even", Ecount)
print("Odd", Ocount)

#Question-5
count = 0
for i in range(1,101):
    if(i%3 == 0 and i%5 == 0):
        count = count + 1
print(count)

#Question-6
sum = 0
for i in range(1,6):
    sum = sum + i
print(sum)

#Question-7
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

#Question 8:
sum = 0
n = int(input("Enter Number:"))
print( "The First ", n ," natural number is : ")
if(n>0):
    for i in range(n):
        print(i+1)
        sum = sum + i
    print("sum :", sum)
else:
    print("Not an Natural Number")

#Question-9
import math
num = int(input("Input number of Terms: "))
for i in range(num):
    cub = math.pow(i+1,3) 
# (Or) num**(3)  raise the number to the power of 3, ** -> exponential
# if it is cubic root use 1/3
    print(i+1, " and cube of the ", i+1, " is : ",cub )

#Question10-Pattern Question:
for i in range(1,5):
    print()#Gap
    for j in range(1,i+1):
        print("*", end="")

#i=1   j(1,2)->j=1
#i=2   j(1,3)->j=1,2
#i=3   j(1,4)->j=1,2,3
#i=4   j(1,5)->1,2,3,4