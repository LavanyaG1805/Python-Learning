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