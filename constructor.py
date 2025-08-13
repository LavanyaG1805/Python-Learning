# A constructor is a unique function that gets called automatically when an object is created of a class.
# init is a inbulid constructor given by python. we are bit created it.

# constructor -> how much the constructor size is and where to store it. how much allocation need to give.

# All classes have a method called __init__(), 
# which is always executed when the class is being initiated.

# Use the __init__() method to assign values to object properties, 
# or other operations that are necessary to do when the object is being created

class laptop:
    def __init__(self):#constructor
        print("demo")
    def display(self):
        print("Display")

HP = laptop()

#Once i created the object it automatically call the init constructor.
#---------------------------------------------

#Before we declare the variable like this in [class and object]
class laptop:
    ram = ""
    processor = ""
    def __init__(self):#constructor
        print("demo")
    def display(self):
        print("Display")

HP = laptop()

#----------------------------------------------
#[but now we should create like this]
#The main purpose of a constructor is to initalize or assign values to the data members of that class.

class laptop:
    def __init__(self):#constructor
        self.ram=""
        self.processor=""
        print("demo")
    def display(self):
        print("Display")

HP = laptop()

HP.ram = "8GB"
HP.processor = "i5"

print(HP.ram)
# here we are calling the value

#-----------------------------------------
#Method:

class laptop: # step 1 - Creation of class
    def __init__(self):# step 3 -> create the variable HP.RAM and HP.processor
        # step 5 -> now create the variable dell.ram and dell.processor
        self.ram=""
        self.processor=""
    def display(self):
        # step 8 -> def display(hp) -> whereever self is there it will replace with hp. becoz it refer the object.
        print("ram: ", self.ram) # step 9 ->print(ram: hp.ram=8GB) -> ram: 8GB
        print("processor: ", self.processor) # step 10

HP = laptop() # Step 2 -> to creation of object.
# when you create that object it autmatically call the constructor.
#it will be like HP = laptop(HP)
dell = laptop() # Step 4 -> call constructor. it wil look like dell = laptop(dell)

#Sep 6 -> assign the values 
HP.ram = "8GB"
HP.processor = "i5"

dell.ram = "16GB"
dell.processor = "i7"

#step 7: hp.display(hp) -> call display function
HP.display()
dell.display() # step 11 -> same as step 7


# self -> The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.