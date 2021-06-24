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

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = [rock, paper, scissors]

comp_rand = (random.choice(comp_choice))

if choice == 0:
  print(rock)
  print(f"Computer chose:\n{comp_rand}")
  if comp_rand == rock:
    print("It's a draw, you can go again")
  elif comp_rand == paper:
    print("You lose.")
  elif comp_rand == scissors:
    print("You win!")
elif choice == 1:
  print(paper)
  print(f"Computer chose:\n{comp_rand}")
  if comp_rand == rock:
    print("You win!")
  elif comp_rand == paper:
    print("It's a draw, you can go again")
  elif comp_rand == scissors:
    print("You lose.")
elif choice == 2:
  print(scissors)
  print(f"Computer chose:\n{comp_rand}")
  if comp_rand == rock:
    print("You lose.")
  elif comp_rand == paper:
    print("You win!")
  elif comp_rand == scissors:
    print("It's a draw, you can go again")
else:
  print("You type an invalid number. So you lose!")           


