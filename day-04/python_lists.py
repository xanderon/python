import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

rantom_person_int = random.randint(0, len(names)-1)
print(f"This person is going to pay: {names[rantom_person_int]}")

#random.choice(names) -> selects random name