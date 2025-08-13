# In Boolean True, False = First letter should be capital
if(True):
    print("YES")
else:
    print("No")

# "==" is one of the comparision operator
# The result of comprision operator will be either True or False
# if block or else block, only one of them will work according to the condition.
rcb = "win"
if(rcb == "win"):
    print("RCB won")
else:
    print("RCB Loss")

#"if" condition there means there is no complusory to have "else" condition
#Question 6
Score1 = int(input("Enter The Score:"))
if(Score1 <= 100):
    if(Score1 < 35):
        print("Poor Student")
    elif(70>Score1>35):
        print("Average Student")
    elif(Score1 > 70):
        print("Good Student")
else:
    print("Invalid Score")

# Score -> 65, Output -> Average.
# instead of elif you can also use if condition but what's the drawback is 
# it will print the output in second condition itself as Average Student, 
# though it will check the rest of the all "if" condition like Good Student and
#  so on, so move to elif. in elif it will stop at that condition itself.



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