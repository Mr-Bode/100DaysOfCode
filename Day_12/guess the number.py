logo = """
   _____                          _______  _             _   _                    _                  _ 
  / ____|                        |__   __|| |           | \ | |                  | |                | |
 | |  __  _   _   ___  ___  ___     | |   | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ | |
 | | |_ || | | | / _ \/ __|/ __|    | |   | '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|| |
 | |__| || |_| ||  __/\__ \\__ \    | |   | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   |_|
  \_____| \__,_| \___||___/|___/    |_|   |_| |_| \___| |_| \_| \__,_||_| |_| |_||_.__/  \___||_|   (_)

  """


import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
random_answer = random.randint(1, 100)
#print(f"Pssst, the correct answer is {random_answer}")

def guessing():
  guess = int(input("Make a guess: "))
  return guess


def choose_difficulty(tries):
  attempts = tries
  print(f"You have {tries} attempts to guess the number.")
  while attempts != 0:
    my_guess = guessing()
    if my_guess == random_answer:
      attempts = 0
      print(f"You got it! The answer was {my_guess}")
    elif my_guess > random_answer:
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Too high")
        print("Guess again.")
        print(f"You have {attempts} remaining to guess the number.")
    elif my_guess < random_answer:
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Too low")
        print("Guess again.")
        print(f"You have {attempts} remaining to guess the number.")
      

choose = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choose == "easy":
  choose_difficulty(10)
elif choose == "hard":
  choose_difficulty(5)