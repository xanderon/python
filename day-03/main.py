# #If / Else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# age = int(input("What is your age? "))
# if height >= 120:
#     print("You can ride the rollercoaster")
#     if age < 12:
#         print("Child tickets are $5")
#         bill = 5
#     elif age <=18:
#         print("Youth tickets are $7")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Middle Aged PPl tickets are $0")
#         bill = 0
#     else:
#         print("Adult tickets are $12")
#         bill = 12
#     wants_photo = input("Do you want a photo taken? Y or N?")
#     if wants_photo == "Y":
#         #Add $3 to their bill
#         bill += 3
#     print(f"your bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# # #Odd or Even
# # number = int((input("What number do you want to check? ")))
# # if number % 2 == 0:
# #     print("The number is even!")
# # else:
# #     print("The number is odd!")

# #Leap Year
# year = int(input("Leap Year Checker. What year do you want to check? "))
# is_divisible_by_4 = (year % 4) == 0
# is_divisible_by_100 = (year % 100) == 0
# is_divisible_by_400 = (year % 400) == 0

# if is_divisible_by_4:
#     if is_divisible_by_100:
#         if is_divisible_by_400:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Pizza Order
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# price = 0
# if size == "S":
#     price = 15
# if size == "M":
#     price = 20
# if size == "L":
#     price = 25
# if add_pepperoni == "Y":
#     if size == "S":
#         price += 2
#     else:
#         price += 3

# if extra_cheese == "Y":
#     price += 1
# print(f"Your final bill is: ${price}.")

#Love Calculator

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# combined_name = (name1 + name2).lower()

# T = 0
# R = 0
# U = 0
# E = 0

# L = 0
# O = 0
# V = 0
# E = 0

# #name1
# T += combined_name.count("t")
# R += combined_name.count("r")
# U += combined_name.count("u")
# E += combined_name.count("e")

# L += combined_name.count("l")
# O += combined_name.count("o")
# V += combined_name.count("v")

# total1 = T + R + U + E
# total2 = L + O + V + E

# love_score = int(f"{str(total1)}{str(total2)}")
# message = f"Your score is {love_score}"

# if love_score <= 10 or love_score > 90:
#     message += ", you go together like coke and mentos."
# elif love_score >= 40 and love_score <= 50:
#     message += ", you are alright together."

# print(message)

