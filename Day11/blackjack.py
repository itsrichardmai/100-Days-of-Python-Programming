import random 

cards = {
      "a": 1,
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8":8,
      "9":9,
      "10":10,
      "J":10,
      "Q":10,
      "K":10
}

balance = 100

def blackjack():

      print(f'''
                        .------.------.------.------.
                        |A_  _ |A /\  |A _   |A .   |
                        |( \/ )| /  \ | ( )  | / \  |
                        | \  / | \  / |(_x_) |(_,_) |
                        |  \/ A|  \/ A|  Y  A|  I  A|
                        `------^------^------'------'
            
            Welcome to Blackjack! Place your bets!
            Your balance is: ${balance}
            ''')

      bet = int(input("How much would you like to bet?: $"))
      print("Bets are closed!") 

      if bet > balance:
            print("You do not have enough balance to place this bet!")
            blackjack()
      elif bet <= balance:
            card, value = random.choice(list(cards.items()))
            card2, value2 = random.choice(list(cards.items()))
            card3, value3 = random.choice(list(cards.items()))
            player_score = value + value2
            print(f"You drew: {card} and {card2} your total is {(player_score)}")
            print(f"Dealer shows {card3} and has a total of {value3}")
            dealer_score = value3 
            while player_score <= 21:
                  decision = input("Type 'h' for hit. 's' for stand. 'x' for surrender!").lower()
                  if decision == 'h':
                        card4, value4 = random.choice(list(cards.items()))
                        player_score += value4
                        print(f"You drew a {card4} Your total is {player_score}")
                  elif decision == 's':
                        while dealer_score <= 17:
                              print("Dealer's draw!")
                              card5, value5 = random.choice(list(cards.items()))
                              dealer_score += value5
                              print(f"Dealer drew a {card5}, their total is {dealer_score}")
                              if dealer_score > 21:
                                    print("Dealer bust! You win")
                                    balance += bet 
                              elif dealer_score > player_score:
                                    print("You lost! Dealer has {dealer_score}")
                              elif dealer_score == player_score:
                                    print("It's a tie!")
                              elif dealer_score == 21 and player_score == 21:
                                    print("It's a tie!")
                              elif dealer_score == 21 and player_score != 21:
                                    print("You lose! Dealer has 21!")
                              

                  



blackjack()