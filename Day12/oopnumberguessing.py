import random
from art import logo


class NumberGuessingGame:
    """A number guessing game with different difficulty levels."""
    
    # Constants for better maintainability
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    EASY_LIVES = 10
    HARD_LIVES = 5
    
    def __init__(self):
        """Initialize the game with default values."""
        self.target_number = 0
        self.lives = 0
        self.game_over = False
    
    def display_welcome(self):
        """Display welcome message and game logo."""
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}")
    
    def get_difficulty(self):
        """Get and validate difficulty choice from user."""
        while True:
            difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower().strip()
            
            if difficulty == 'easy':
                return self.EASY_LIVES
            elif difficulty == 'hard':
                return self.HARD_LIVES
            else:
                print("❌ Invalid option! Please type 'easy' or 'hard'.")
    
    def get_user_guess(self):
        """Get and validate user's number guess."""
        while True:
            try:
                guess = int(input(f"\nGuess a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}: "))
                
                if self.MIN_NUMBER <= guess <= self.MAX_NUMBER:
                    return guess
                else:
                    print(f"❌ Please enter a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}!")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def evaluate_guess(self, user_guess):
        """Evaluate the user's guess and provide feedback."""
        if user_guess > self.target_number:
            print("📉 Too high! The number is lower.")
            return False
        elif user_guess < self.target_number:
            print("📈 Too low! The number is higher.")
            return False
        else:
            print(f"🎉 Congratulations! You guessed it! The number was {self.target_number}!")
            return True
    
    def play_round(self):
        """Play a single round of the guessing game."""
        self.target_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        self.lives = self.get_difficulty()
        
        print(f"\n🎯 You have {self.lives} attempts to guess the number!")
        
        # Uncomment for debugging: print(f"DEBUG: Target number is {self.target_number}")
        
        while self.lives > 0:
            print(f"\n💖 Lives remaining: {self.lives}")
            
            user_guess = self.get_user_guess()
            correct_guess = self.evaluate_guess(user_guess)
            
            if correct_guess:
                return True  # Player won
            
            self.lives -= 1
            
            if self.lives == 0:
                print(f"\n💀 Game Over! The number was {self.target_number}")
                return False  # Player lost
    
    def ask_play_again(self):
        """Ask user if they want to play again."""
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y']:
                return True
            elif play_again in ['no', 'n']:
                return False
            else:
                print("❌ Please enter 'yes' or 'no'.")
    
    def play(self):
        """Main game loop."""
        self.display_welcome()
        
        games_played = 0
        games_won = 0
        
        while True:
            games_played += 1
            print(f"\n{'='*50}")
            print(f"🎮 GAME {games_played}")
            print('='*50)
            
            if self.play_round():
                games_won += 1
            
            if not self.ask_play_again():
                break
        
        # Display final statistics
        print(f"\n📊 Game Statistics:")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        print(f"Win rate: {(games_won/games_played)*100:.1f}%")
        print("\nThanks for playing! 👋")


def main():
    """Main function to run the game."""
    game = NumberGuessingGame()
    game.play()


if __name__ == '__main__':
    main()