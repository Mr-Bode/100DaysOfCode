from game_data import data
from replit import clear
import random
from art import logo, vs

A = random.choice(data)
B = random.choice(data)

if A == B:
  B = random.choice(data)

end_of_game = False
score = 0

def get_score(num_score):
  return num_score

def format_stats(info):
  fact = [info["name"], info["description"], info["country"]]
  return fact

def stats_result(first, second):
  clear()
  first_fact = format_stats(first)
  second_fact = format_stats(second)
  final_score = get_score(score)
  print(logo)
  print(f"You're right! Current score: {final_score}")
  print(f"Compare A: {first_fact[0]}, a {first_fact[1]}, from {first_fact[2]}")
  print(vs)
  print(f"Against B: {second_fact[0]}, a {second_fact[1]}, from {second_fact[2]}")
  

def compare(first, second):
  f_first = first["follower_count"]
  f_second = second["follower_count"]
  if f_first < f_second:
    return 0
  else:
    return 1

def endgame(final_score):
  global end_of_game
  clear()
  print(logo)
  print(f"Sorry, that's wrong. Final score: {final_score}")
  end_of_game = True

#Print initial A vs B
print(logo)
print(f'Compare A: {A["name"]}, {A["description"]}, from {A["country"]}')
print(vs)
print(f'Against B: {B["name"]}, {B["description"]}, from {B["country"]}')

while not end_of_game:
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  # Guess conditions
  if guess == "A":
    answer = compare(A, B)
    if answer == 1:
      score += 1
      A = B
      B = random.choice(data)
      stats_result(A, B)
    else:
      endgame(score)
  elif guess == "B":
    answer = compare(B, A)
    if answer == 1:
      score += 1
      A = B
      B = random.choice(data)
      stats_result(A, B)
    else:
      endgame(score)
  else:
    endgame(score)
