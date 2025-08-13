#Question-1
a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

add()
sub()
mul()

#Question-2
def findevenodd(num):
    if(num%2==0):
        print("It is a Even Number")
    else:
        print("It is a Odd Number")

value = int(input("Enter Number:"))
findevenodd(value)

#Question-3:
def findpassorfail(mark):
    if(mark>35):
        print("Passed in this course")
    else:
        print("Failed in this course")

a = int(input("Enter Your Marks:"))
findpassorfail(a)

#Question-4:
def printrange(num1,num2):
    for i in range(num1,num2+1):
        print(i)
a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
printrange(a,b)

#Question -5(Return)
s_username = "EMC"
s_password ="123"
uname = input("Enter Your User Name: ")
pwd = input("Enter Your Password: ")
def validate():
    if(uname == s_username and pwd == s_password):
        return True
    else:
        return False
    
result = validate()
print(result)

#Question - 6
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

def add():
    d = a +b
    e = d*c
    return e

res = add()
print(res)



