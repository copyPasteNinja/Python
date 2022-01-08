name = str(input("Hello welcome to FuchiGO, what is your name?: "))
age = str(input("How old are you?: "))
request = str(input("What can we do for you?: "))

services = ["Migrations", "Integration", "Infrustructure", "Consulting"]

if request.capitalize() in services:
  service = str(input("Do you need" + services[0] + "Or" + services[1] + "Or" + services[2] + "Or" + services[3] + "?")
  if service == "Migration":
       print("Migrating to Cloud is Great Choice")


elif age() < 10:
    print("You're too young to bee ")


else: 
    print("You are not welocome here!")

