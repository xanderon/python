#Tip: use Thonny for cool debugging
##Basic log
print("🚨 Learning Python 🚨")

##Using new line /n
#print("print('what to print')\nTest\nTest\nTest")

##Calling input
#print("Hello " + input("What is your name?"))

##Ex: Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string. 
#print(len(input("What is your name?")))

##Variables
#name = input("What is your name?")
#print(name)

##Ex: Write a program that switches the values stored in the variables a and b.

# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# c = a
# a = b
# b = c
# #Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)


## Ex: Band Name Generator

#1. Create a greeting for your program.
print("Hi there! Wellcome to the band name generator!")
#2. Ask the user for the city that they grew up in.
city_name = input("What is the city you grew up in?\n")
print(city_name)
#3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n")
print(pet_name)
#4. Combine the name of their city and pet and show them their band name.
print("New Band Name: " + city_name + " " + pet_name + ". This name rocks!")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/