import random 
from game_data import data 
from art import logo 
class HLGame: 
    def __init__(self):
        """Initialize the Higher/Lower game"""
        self.score = 0
        self.game_data = data
        self.current_person = None
        self.next_person = None
    
    def display_welcome(self):
        """Display welcome message and game logo."""
        print(logo)  # Use the imported logo, not self.logo
        print("Welcome to the Higher or Lower Game!")
        print("Guess who has more followers!\n")
    
    def get_random_person(self):
        """Get a random person from the data"""
        return random.choice(self.game_data)
    
    def format_person(self, person):
        """Format person data for display"""
        return f"{person['name']}: {person['description']}"
    
    def compare_followers(self, person1, person2, user_choice):
        """Compare followers and return if user was correct"""
        person1_followers = person1['follower_count']
        person2_followers = person2['follower_count']
        
        if user_choice.lower() == 'a':
            return person1_followers > person2_followers
        else:  # user_choice == 'b'
            return person2_followers > person1_followers
    
    def play_round(self):
        """Play a single round of the game"""
        # Get two different people
        self.current_person = self.get_random_person()
        self.next_person = self.get_random_person()
        
        # Make sure they're different
        while self.current_person == self.next_person:
            self.next_person = self.get_random_person()
        
        # Display the comparison
        print(f"Compare A: {self.format_person(self.current_person)}")
        print("VS")
        print(f"Against B: {self.format_person(self.next_person)}")
        
        # Get user's guess
        while True:
            choice = input("\nWho has more followers? Type 'A' or 'B': ").strip().upper()
            if choice in ['A', 'B']:
                break
            print("Please enter 'A' or 'B' only!")
        
        # Check if user was correct
        is_correct = self.compare_followers(self.current_person, self.next_person, choice)
        
        if is_correct:
            self.score += 1
            print(f"\n✅ You're right! Current score: {self.score}")
            print(f"\n {self.current_person['name']} has {self.current_person['follower_count']} followers")
            print(f"\n {self.next_person['name']} has {self.next_person['follower_count']} followers")
            return True
        else:
            print(f"\n❌ Sorry, that's wrong. Final score: {self.score}")
            # Show the actual follower counts
            print(f"{self.current_person['name']} has {self.current_person['follower_count']:,} followers")
            print(f"{self.next_person['name']} has {self.next_person['follower_count']:,} followers")
            return False
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            continue_game = self.play_round()
            
            if not continue_game:
                print("Game Over!")
                break
            
            print("-" * 50)


# Alternative: Using functions instead of a class (simpler approach)
def display_welcome_function():
    """Function version - no self parameter needed"""
    print(logo)
    print("Welcome to the Higher or Lower Game!")

def main():
    """Main function to run the game"""
    # Option 1: Using the class (Object-Oriented approach)
    game = HLGame()  # Create an instance of the class
    game.play_game()  # Call the method on the instance
    
    # Option 2: Using functions (Procedural approach)
    # display_welcome_function()  # Call function directly

if __name__ == '__main__':
    main()