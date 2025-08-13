#Question 1:
class laptop:
    Price = 0 #to define it as integer
    Processor = ""
    RAM = ""

HP = laptop() #now hp laptop wants to use this laptop so, they will set their own price,processor and RAM
Lenovo = laptop()
DELL = laptop()

HP.Price = 50000
HP.Processor = "i5"
HP.RAM = "8GB"

Lenovo.Price = 60000
Lenovo.Processor = "i7"
Lenovo.RAM = "16gb"

DELL.Price = 80000
DELL.Processor = "i11"
DELL.RAM = "24GB"

print(DELL.RAM)

#if you want to do the same without object and class means 
# you want to create variable for everything it will be increase the time and space. in this we just accessing the object.
#it is effecient and we can reuse it.

#Question - 2
class Tiruvannamalai():
    girivalam = ""
    Temple = ""
    Ashram = ""
    def Timegirivalam(self):
        print("It will take upto 5 to 6 hrs")
    def TimeTemple(self):
        print("for queue it take 2 hrs")
    def TimeAshram(self):
        print("visit quickly")

ramesh = Tiruvannamalai()
suresh = Tiruvannamalai()
mahesh = Tiruvannamalai()

ramesh.girivalam = "14 Km"
print(ramesh.girivalam)
ramesh.Timegirivalam()

suresh.Temple = "9 Gopuram"
print(suresh.Temple)
suresh.TimeTemple()

mahesh.Ashram = "Ramana Asharam"
print(mahesh.Ashram)
mahesh.TimeAshram()

# Question - 3
class student():
    def __init__(self):
        self.name = ""
        self.rno = ""

    def display(self):
        print("Name: ", self.name)
        print("Register Number: ", self.rno)

s1 = student()
s2 = student()

s1.name = "Lavanya"
s1.rno = "CH.EN.U4AIE21166"

s2.name = "Shyam Ganesh"
s2.rno = "CH.EN.U4AIE21149"

s1.display()
s2.display()

#Question - 4
