import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# generate random 1 - 3

randomOption = random.randint(0, 2)
optionList = [rock, paper, scissors]
oponentOption = optionList[randomOption]

playerOptionIndex = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if not (playerOptionIndex >= 0 and playerOptionIndex <= 2):
    print(f"Error: The option {playerOptionIndex} is invalid, please try again. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    exit()
    
playerOption = optionList[playerOptionIndex]

if playerOption == rock:
    if oponentOption == scissors:
        print(f"\nYou win! 🎂 \n{rock} \nbeats {scissors}.")
    else:
        print(f"\nYou loose! 😢 \n{paper} \nbeats {rock}.")
if playerOption == paper:
    if oponentOption == rock:
        print(f"\nYou win! 🎂 \n{paper} \nbeats {rock}.")
    else:
        print(f"\nYou loose! 😢 \n{scissors} \nbeats {paper}.")
if playerOption == scissors:
    if oponentOption == paper:
        print(f"\nYou win! 🎂 \n{scissors} \nbeats {paper}.")
    else:
        print(f"\nYou loose! 😢 \n{rock} \nbeats {paper}.")
elif oponentOption == rock:
        print(f"\nDraw! \nBoth selected {rock} {rock}.")
