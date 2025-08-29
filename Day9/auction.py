# start 

# show logo from art.py

# ask for name input 

# ask for bid price

# add name and bid into a dictionary as the key and value

# ask if there are other users who want to bid

# yes? -> clear the screen -> ask for name input 

# no ? -> find the highest bid in the dictionary and declare them the winner 
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
      \n
      ''')

bids = {}
continue_bidding = True
while continue_bidding == True:
  name = input("Hello! Welcome to the Silent Auction! What is your name?: ")
  price= float(input("How much would you like to bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == 'no':
    continue_bidding = False
    highest_bid = 0
    highest_bidder = ""
    for key in bids:
      if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key
    print(f"The winner is: {highest_bidder}! for a price of {highest_bid}\nCongratulations, {highest_bidder}! ")
     
