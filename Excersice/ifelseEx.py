# Question 1
Meghna = input("Meghna Lived or Died?")
if(Meghna == "Died"):
    print("Surya Meets Priya")
else:
    print("Surya weds Meghna")

# Question 2
Mark = int(input("Enter Your Mark:"))
if(Mark > 35):
    print("PASS")
else:
    print("FAIL")

# Question 3
income = int(input("Enter Your Income:"))
if(income > 7000):
    print("Not Eligible for Scholarship")
else:
    print("Eligible for Scholarship")

#Question 4
num = int(input("Enter Number:"))
if (num%3 == 0 and num%5 == 0):
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3 and 5")

#Question 5
number = int(input("Enter The Number:"))
if (number%2 == 0):
    print("It is a Even Number")
else:
    print("Its a Odd Number")

#Question 6
Score1 = int(input("Enter The Score:"))
if(Score1 <= 100):
    if(Score1 < 35):
        print("Poor Student")
    elif(70>Score1>35):
        print("Average Student")
    elif(Score1 > 70):
        print("Good Student")

#Question 7
a = int(input("Enter The Number a:"))
b = int(input("Enter The Number b:"))
cal = input("Enter The Operation:")
if(cal == "add"):
    print("Result", a+b)
elif(cal == "sub"):
    print("Result", a-b)
elif(cal == "mul"):
    print("Result", a*b)
elif(cal == "div"):
    print("Result", a/b)
else:
    print("Invalid Operation")

#Question 8
percentage = int(input("Enter The Percentage:"))
if (percentage >= 70):
    Name = input("Enter The Name:")
    Department = input("Enter The Department:")
    Location = input("Enter The Location:")
    print("Eligible")
else:
    print("Not Eligible")

#Question 9
# Here we are using "if" condition inside the "if" condition -> Nested if
salary = int(input("Enter Your Salary:"))
age = int(input("Enter Your Age:"))
if(salary >= 20000 or age <= 25):
    loan = int(input("Enter The Loan Amount:"))
    if(loan <= 50000):
        print("Eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("not eligible for Loan")

#Question 10
mat = int(input("Enter Maths Mark:"))
sci = int(input("Enter Science Mark:"))
ss = int(input("Enter Social Science Mark:"))
eng = int(input("Enter English Mark:"))
tam = int(input("Enter Tamil Mark:"))
avg = mat + sci + ss + eng + tam / 5
if (avg < 35):
    print("Additional Class is Required")
else:
    print("You are good to go")

#Question 11 (HackerRank)
n = int(input())
if (n%2 == 1):
    print("Weird")
else:
    if( 2 <= n <= 5):
        print("Not Weird")
    elif(6<=n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")