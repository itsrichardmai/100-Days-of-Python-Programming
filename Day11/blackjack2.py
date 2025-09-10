import random
import os
import time

class Card:
    """Represents a single playing card with only numeric value (1-13)"""
    
    def __init__(self, value):
        self.value = value
    
    def get_display_value(self):
        """Return the display representation of the card"""
        if self.value == 1:
            return 'A'
        elif self.value == 11:
            return 'J'
        elif self.value == 12:
            return 'Q'
        elif self.value == 13:
            return 'K'
        else:
            return str(self.value)
    
    def get_blackjack_value(self):
        """Return the blackjack value of the card"""
        if self.value == 1:  # Ace
            return 11
        elif self.value > 10:  # Face cards
            return 10
        else:
            return self.value
    
    def __str__(self):
        return self.get_display_value()

class Hand:
    """Represents a hand of cards"""
    
    def __init__(self):
        self.cards = []
        self.aces = 0
    
    def add_card(self, card):
        """Add a card to the hand"""
        self.cards.append(card)
        if card.value == 1:  # Ace
            self.aces += 1
    
    def get_value(self):
        """Calculate the best possible value of the hand"""
        total = 0
        aces = self.aces
        
        for card in self.cards:
            total += card.get_blackjack_value()
        
        # Adjust for aces
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        
        return total
    
    def is_blackjack(self):
        """Check if hand is a natural blackjack"""
        return len(self.cards) == 2 and self.get_value() == 21
    
    def is_bust(self):
        """Check if hand is busted"""
        return self.get_value() > 21
    
    def display(self, hide_first=False):
        """Display the hand"""
        if hide_first and len(self.cards) > 0:
            return "[Hidden], " + ", ".join([str(card) for card in self.cards[1:]])
        return ", ".join([str(card) for card in self.cards])
    
    def clear(self):
        """Clear the hand"""
        self.cards = []
        self.aces = 0

class Deck:
    """Represents an infinite deck that generates random cards"""
    
    def deal_card(self):
        """Deal a random card with value 1-13"""
        value = random.randint(1, 13)
        return Card(value)

class Player:
    """Represents a player"""
    
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.hand = Hand()
        self.current_bet = 0
    
    def place_bet(self, amount):
        """Place a bet"""
        if amount <= self.money and amount > 0:
            self.current_bet = amount
            self.money -= amount
            return True
        return False
    
    def win_bet(self, multiplier=2):
        """Win the current bet"""
        winnings = self.current_bet * multiplier
        self.money += winnings
        return winnings
    
    def push_bet(self):
        """Push (tie) - get bet back"""
        self.money += self.current_bet
    
    def reset_bet(self):
        """Reset the current bet"""
        self.current_bet = 0

class BlackjackGame:
    """Main Blackjack game class"""
    
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer_hand = Hand()
        self.game_over = False
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_game_state(self, hide_dealer_card=True):
        """Display the current game state"""
        print("=" * 50)
        print("🎲 BLACKJACK GAME 🎲")
        print("=" * 50)
        print(f"💰 Money: ${self.player.money}")
        print(f"🎯 Current Bet: ${self.player.current_bet}")
        print()
        
        # Dealer's hand
        print("🎴 Dealer's Hand:")
        if hide_dealer_card:
            print(f"   Cards: {self.dealer_hand.display(hide_first=True)}")
            if len(self.dealer_hand.cards) > 1:
                # Show value without hidden card
                visible_value = sum(card.get_blackjack_value() for card in self.dealer_hand.cards[1:])
                print(f"   Value: {visible_value} + Hidden")
        else:
            print(f"   Cards: {self.dealer_hand.display()}")
            print(f"   Value: {self.dealer_hand.get_value()}")
        print()
        
        # Player's hand
        print("👤 Your Hand:")
        print(f"   Cards: {self.player.hand.display()}")
        print(f"   Value: {self.player.hand.get_value()}")
        print()
    
    def get_bet(self):
        """Get bet amount from player"""
        while True:
            try:
                print(f"💰 Available money: ${self.player.money}")
                bet = int(input("Enter your bet amount: $"))
                
                if bet <= 0:
                    print("❌ Bet must be greater than 0!")
                    continue
                elif bet > self.player.money:
                    print("❌ You don't have enough money!")
                    continue
                else:
                    return bet
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def initial_deal(self):
        """Deal initial cards"""
        # Deal two cards to player and dealer
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
    
    def player_turn(self):
        """Handle player's turn"""
        while True:
            self.display_game_state()
            
            # Check for bust
            if self.player.hand.is_bust():
                print("💥 BUST! You went over 21!")
                return False
            
            # Check for 21
            if self.player.hand.get_value() == 21:
                print("🎯 You have 21!")
                return True
            
            # Get player action
            print("Choose your action:")
            print("1. Hit (take another card)")
            print("2. Stand (keep current hand)")
            
            try:
                choice = input("Enter choice (1 or 2): ").strip()
                
                if choice == '1':
                    # Hit
                    new_card = self.deck.deal_card()
                    self.player.hand.add_card(new_card)
                    print(f"🎴 You drew: {new_card}")
                    time.sleep(1)
                elif choice == '2':
                    # Stand
                    return True
                else:
                    print("❌ Invalid choice! Please enter 1 or 2.")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing!")
                exit()
    
    def dealer_turn(self):
        """Handle dealer's turn"""
        print("\n🎴 Dealer's turn...")
        time.sleep(1)
        
        while self.dealer_hand.get_value() < 17:
            new_card = self.deck.deal_card()
            self.dealer_hand.add_card(new_card)
            print(f"🎴 Dealer draws: {new_card}")
            self.display_game_state(hide_dealer_card=False)
            time.sleep(1.5)
        
        print(f"🎴 Dealer stands with {self.dealer_hand.get_value()}")
    
    def determine_winner(self):
        """Determine the winner and handle payouts"""
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        player_blackjack = self.player.hand.is_blackjack()
        dealer_blackjack = self.dealer_hand.is_blackjack()
        
        print("\n" + "=" * 50)
        print("🏆 GAME RESULTS")
        print("=" * 50)
        
        # Player busted
        if self.player.hand.is_bust():
            print("💥 You busted! Dealer wins!")
            return
        
        # Dealer busted
        if self.dealer_hand.is_bust():
            print("💥 Dealer busted! You win!")
            winnings = self.player.win_bet()
            print(f"💰 You won ${winnings}!")
            return
        
        # Both have blackjack
        if player_blackjack and dealer_blackjack:
            print("🤝 Both have Blackjack! It's a push!")
            self.player.push_bet()
            return
        
        # Player has blackjack
        if player_blackjack:
            print("🎉 BLACKJACK! You win!")
            winnings = self.player.win_bet(2.5)  # Blackjack pays 3:2
            print(f"💰 You won ${winnings}!")
            return
        
        # Dealer has blackjack
        if dealer_blackjack:
            print("😔 Dealer has Blackjack! You lose!")
            return
        
        # Compare values
        if player_value > dealer_value:
            print("🎉 You win!")
            winnings = self.player.win_bet()
            print(f"💰 You won ${winnings}!")
        elif player_value < dealer_value:
            print("😔 Dealer wins!")
        else:
            print("🤝 It's a push!")
            self.player.push_bet()
    
    def play_round(self):
        """Play a single round"""
        # Reset hands
        self.player.hand.clear()
        self.dealer_hand.clear()
        
        # Get bet
        bet_amount = self.get_bet()
        if not self.player.place_bet(bet_amount):
            print("❌ Invalid bet!")
            return
        
        # Initial deal
        self.initial_deal()
        
        # Check for initial blackjack
        if self.player.hand.is_blackjack() or self.dealer_hand.is_blackjack():
            self.display_game_state(hide_dealer_card=False)
            self.determine_winner()
        else:
            # Player's turn
            if self.player_turn():
                # Dealer's turn only if player didn't bust
                if not self.player.hand.is_bust():
                    self.dealer_turn()
            
            # Show final hands and determine winner
            self.display_game_state(hide_dealer_card=False)
            self.determine_winner()
        
        # Reset bet
        self.player.reset_bet()
    
    def play(self):
        """Main game loop"""
        print("🎉 Welcome to Blackjack!")
        print("Goal: Get as close to 21 as possible without going over!")
        print("Face cards (J, Q, K) are worth 10. Aces are worth 1 or 11.")
        print("Blackjack (21 with first 2 cards) pays 3:2!")
        input("\nPress Enter to start...")
        
        while True:
            self.clear_screen()
            
            # Check if player has money
            if self.player.money <= 0:
                print("💸 You're out of money! Game Over!")
                break
            
            # Play a round
            self.play_round()
            
            # Ask to continue
            print(f"\n💰 Current money: ${self.player.money}")
            while True:
                continue_game = input("\nPlay another round? (y/n): ").lower().strip()
                if continue_game in ['y', 'yes']:
                    break
                elif continue_game in ['n', 'no']:
                    print("👋 Thanks for playing Blackjack!")
                    print(f"💰 Final money: ${self.player.money}")
                    return
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")

# Run the game
if __name__ == "__main__":
    game = BlackjackGame()
    try:
        game.play()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing Blackjack!")