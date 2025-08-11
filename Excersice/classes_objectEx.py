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
