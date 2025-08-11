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
