import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  choice_card = random.choice(cards)
  return choice_card

def calculate_score(card_list):
  """Take a list of cards and return the score calculated from the cards"""
  card_score = sum(card_list)
  if 11 in card_list and 10 in card_list and len(card_list) == 2:
    return 0  
  if 11 in card_list and card_score > 21:
    card_list.remove(11)
    card_list.append(1)
    card_score = sum(card_list)
  return card_score

def compare(user, computer):
  if user == computer:
    print("Same hands for both of you. It's a draw")
  elif computer == 0:
    print("Opponent has a blackjack! You lose")
  elif user == 0:
    print("You've gotten a blackjack! You win")
  elif user > 21:
    print("You went over. You lose")
  elif computer > 21:
    print("Opponent went over. You win")
  elif user > computer:
    print("You have a higher hand. You win")
  elif computer > user:
    print("Opponent has a higher hand. You lose")

def play_blackjack():
  print(logo)
  user_cards = []
  computer_cards = []
  user_continue = True
  for user in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while user_continue:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      user_continue = False
    else:
      answer = input("Type 'y' to get another card, type 'n' to pass: ")
      if answer == "y":
        user_cards.append(deal_card())
      else:
        user_continue = False

  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"    Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

  compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_blackjack()