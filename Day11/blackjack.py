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