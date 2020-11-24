##Data Types

# #String
# print("Hello"[4])

# #Integer
# print(12_3 + 345) # _ is used to read the number like 12,3

# #Boolean
# print(True)
# print(False)

# print(type(1234)) # check the type of the data

# #Type casting
# print("Changing 123 to a string here => " + str(123))

# # Ex: https://repl.it/@appbrewery/day-2-1-exercise#README.md

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# if len(two_digit_number) != 2 :
#     print("Only introduce two digits!")
#     exit()
# two_digit_converted_to_int = int(two_digit_number)
# if type(two_digit_converted_to_int) != type(123) :
#     print("Wrong data type! Only Integers are allowed")
#     exit()
# first_number = int(two_digit_number[0])
# second_number = int(two_digit_number[1])
# print("Result: " + str(first_number + second_number))

# Ex: BMI Calculator https://repl.it/@appbrewery/day-2-2-exercise

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# BMI = float(weight) / float(height) ** 2
# if BMI < 18.5:
#     print("Your BMI is: " + str(BMI) + ". You are Underweight")
# if BMI >= 18.5 and BMI <= 25:
#     print("Your BMI is: " + str(BMI) + ". You are Normal weight")
# if BMI > 25 and BMI <= 30:
#     print("Your BMI is: " + str(BMI) + ". You are Overweight")
# if BMI > 30:
#     print(f"Your BMI is: {BMI}. You are Obese")

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
# # #Write your code below this line 👇
# age = int(age)
# age_remaining = 90 - age
# days = age_remaining * 365
# weeks = age_remaining * 52
# months = age_remaining * 12
# print(f"You have {days} days, {weeks} weeks, and {months} months left")

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15. "))
nr_of_people = int(input("How many people to split the bill? "))
sum_per_person = round(((total_bill / nr_of_people) * (tip_percentage / 100 + 1 )), 3)
print(f"Each person should pay: {sum_per_person}")

#Day 2 Done :)

