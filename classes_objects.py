# Python is an object-oriented language, 
# allowing you to structure your code using classes and objects for better organization and reusability.

# A Class is like an object constructor, or a "blueprint" for creating objects.
#Example: Ramesh and suresh wants to go "goa" but they have different purpose to go to goa like
#Ramesh wants go to goa to drink, party and vibe but, suresh wants to go goa for site seeing, beach
#Here Ramesh and suresh are object and goa is class

class goa:
    name = ""
    drink = ""
    def party(self):
        print("Let's Go Party!!")
    def beach(self):
        print("I Love to see Beach")

#Creation Object
Ramesh = goa() # Ramesh object accesing the goa Class(it is like buying ticket for goa)
Suresh = goa() # Suresh object accesing the goa Class(it is like buying ticket for goa)

Ramesh.name = "Ramesh" #Ramesh and Suresh registering their name in goa 
Suresh.name = "Suresh"

Ramesh.drink = "Yes" #Ramesh and Suresh choosing their preference wheather to drink or not
Suresh.drink = "No"

print("Name: ",Ramesh.name)
print("Drinks: ", Ramesh.drink )
Ramesh.party() #Ramesh wants to do Party

print("Name: ",Suresh.name)
print("Drinks: ", Suresh.drink )
Suresh.beach() #Suresh wnats to see beach

#Modify Object Properties
p1.age = 40

#Delete Object Properties
del p1.age

#Delete Object
del p1
