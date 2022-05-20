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

#Write your code below this line 👇
import random

game = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if game == 0:
  print(rock)
elif game == 1:
  print(paper)
else:
  print(scissors)

print("Computer")

computer_choice = [0, 1, 2]
random_choice = random.choice(computer_choice)

if random_choice == 0:
  print(rock)
elif random_choice == 1:
  print(paper)
else:
  print(scissors)

if game == 0 and random_choice == 0:
  print("Draw!")
elif game == 1 and random_choice == 1:
  print("Draw")
elif game == 2 and random_choice == 2:
  print("Draw!")

if game == 0 and random_choice == 1:
  print("You Lose!")
elif game == 1 and random_choice == 0:
  print("You Win!")

if game == 2 and random_choice == 1:
  print("You Win!")
elif game == 1 and random_choice == 2:
  print("You Lose")

if game == 2 and random_choice == 0:
  print("You Lose!")
elif game == 0 and random_choice == 2:
  print("You Win!")

if game >= 3 or game < 0:
  print("You typed an invalid number. You Lose!")