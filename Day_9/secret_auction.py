logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

end_of_bid = False
bidding = {}

def highest_bid(bid_var):
  highest_price = 0
  winner = ""
  for bidder in bid_var:
    price = bid_var[bidder]
    if price > highest_price:
      highest_price = price
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_price}.")

while not end_of_bid:
  bidder = input("What is your name?: ")
  bid_price = int(input("What's your bid: $"))
  bidding[bidder] = bid_price
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if choice == "yes":
    print("Continue")
  else:
    end_of_bid = True
    highest_bid(bidding)