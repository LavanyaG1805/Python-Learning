#Question-1
i = 1
while(i<=5):
    print(i)
    i = i+1

#Question-2
i = 1
while(i<=20):
    num=i*10
    print(num, end=",")
    i=i+1

#Question-3
i=10
while(i>0):
    print(i, end=",")
    i = i-1

#Question-4(Factorial of Number)
num = int(input("Enter The Number: "))
i = 0 
while(i<num):#0<5
    j=1
    while(j<=i):#1<=5
        mul = mul*j
        j = j+1
i = i+1

#Question-4(Factorial of Number)
num = int(input("Enter The Number: "))#5
fact = 1
while(num>0):
    fact = fact*num
    num = num -1
print(fact)