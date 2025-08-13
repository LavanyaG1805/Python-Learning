#The for loop is usually used when the number of iterations is known. for example: we will give the specific range to it.
#The While loop is usually used when the number of iterations is unknowm.
#some program you can do with both for and while loop. according to your need you can choose.

i = 0 #intialization
while(i==0): # condition
    print(i)
    i = i+1 #incrementation -> without this there is chance of infinite looping

#decerement from 10 to 1
#Question-3
i=10
while(i>0):
    print(i, end=",")
    i = i-1

#Question-4(Factorial of Number)
#5 -> 5*4*3*2*1
num = int(input("Enter The Number: "))#5
fact = 1
while(num>0):
    fact = fact*num
    num = num -1
print(fact)