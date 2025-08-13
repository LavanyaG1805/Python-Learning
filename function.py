# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def painter():
    print("Will Come to paint your house")

painter()

#while it sees the def keyword it will skip that function block and go the next line 
#Which is painter(). now it will call the painter function. it will run now.

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
# div won't work becoz you didn't call div function

#if you didn't call the function means it won't display any output.
#by wrinting the def it won't display anything.

#--------------------------------------------
# Arguments:
# Information can be passed into functions as arguments.
# Arguments are specified after the function name,
#  inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example have one argument(args) as (msg)

def painter(msg):
    print("Message:",msg)

painter("Paint My House")
#when the painter function is called. the message will store in that argument(msg)
# like msg = "Paint My House"

#--------------------
#Paramter or Arguments
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition. Ex: painter(num)
# An argument is the value that is sent to the function when it is called. par(10)

#Number od Arguments -> function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

#-----------------------------------------------------

#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#Output -> The youngest child is Linus

#-------------------------------------------------------

#Keyword Arguments -> You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#Output -> The youngest child is Linus

#------------------------------------------------------

#Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#Output -> His last name is Refsnes

#------------------------------------------------------------

#Default Parameter Value
# If we call the function without argument, 
# it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#I am from Sweden, I am India, I am from norway, I am from brazil

#You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

#---------------------------------------------------------

#Return Keyword
def valueofa(): 
   return 10 # This Function returns 10

a= valueofa() # step 1 -> it call the valueofa function
# step 3 -> a = valueofa()->this function returns 10. so, it become a = 10
print(a) #step 4 -> 10[output]

#Pass Statement -> function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

#------------------------------------------------------

#Postional only argument -> To specify that a function can have only positional arguments, add , / after the arguments
def my_function(x, /):
  print(x)

my_function(3)
#keyword only argument -> To specify that a function can have only keyword arguments, add *, before the arguments
def my_function(*, x):
  print(x)

my_function(x = 3)

#combine positional-only and keyword-only -> Any argument before the / , are positional-only, 
# and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
   