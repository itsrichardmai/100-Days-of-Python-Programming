import turtle  
import pandas as pd  


class StateData:
    """Handles loading and querying the state data from CSV"""
    
    def __init__(self, csv_file='50_states.csv'):
        """Load the CSV data"""
        self.data = pd.read_csv(csv_file)
        # Clean whitespace
        self.data['state'] = self.data['state'].str.strip()
        self.data['abbreviation'] = self.data['abbreviation'].str.strip()
        print(f"Loaded {len(self.data)} states")
    
    def find_state(self, user_input):
        """
        Find a state by name or abbreviation (case-insensitive)
        Returns the state row if found, None if not found
        """
        user_input = user_input.strip()
        
        # Try abbreviation first
        state_row = self.data[self.data['abbreviation'].str.upper() == user_input.upper()]
        
        # If not found, try full name
        if state_row.empty:
            state_row = self.data[self.data['state'].str.lower() == user_input.lower()]
        
        # Return the row if found, None if not
        return state_row if not state_row.empty else None
    
    def get_all_state_names(self):
        """Get list of all state names"""
        return self.data['state'].tolist()
    
    def get_state_info(self, state_row):
        """Extract state name and coordinates from a state row"""
        return {
            'name': state_row['state'].iloc[0],
            'x': int(state_row['x'].iloc[0]),
            'y': int(state_row['y'].iloc[0]),
            'abbr': state_row['abbreviation'].iloc[0]
        }


class GameScreen:
    """Handles the turtle screen and display"""
    
    def __init__(self, image_file='blank_states_img.gif'):
        """Set up the game screen"""
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape(image_file)
        turtle.shape(image_file)
    
    def get_user_input(self, score, total=50):
        """Show input dialog and get user's guess"""
        return self.screen.textinput(
            title=f"{score}/{total} States Correct",
            prompt="Enter state name or abbreviation (Type 'Exit' to quit):"
        )
    
    def write_state_name(self, name, x, y):
        """Write a state name at the given coordinates"""
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(name, align="center", font=("Arial", 8, "normal"))
    
    def show_victory(self):
        """Display victory message"""
        victory = turtle.Turtle()
        victory.hideturtle()
        victory.penup()
        victory.goto(0, 0)
        victory.write("YOU WIN!", align="center", font=("Arial", 36, "bold"))
    
    def keep_open(self):
        """Keep the screen open"""
        self.screen.mainloop()


class GameLogic:
    """Handles the game state and logic"""
    
    def __init__(self):
        """Initialize game state"""
        self.guessed_states = []
        self.total_states = 50
    
    def is_already_guessed(self, state_name):
        """Check if a state has already been guessed"""
        return state_name in self.guessed_states
    
    def add_guess(self, state_name):
        """Add a state to the guessed list"""
        self.guessed_states.append(state_name)
    
    def get_score(self):
        """Get current score"""
        return len(self.guessed_states)
    
    def is_game_complete(self):
        """Check if all states have been guessed"""
        return len(self.guessed_states) >= self.total_states
    
    def get_missed_states(self, all_states):
        """Get list of states that weren't guessed"""
        return [state for state in all_states if state not in self.guessed_states]


class StatesGame:
    """Main game controller that coordinates all components"""
    
    def __init__(self):
        """Initialize all game components"""
        self.state_data = StateData()
        self.screen = GameScreen()
        self.game_logic = GameLogic()
    
    def play(self):
        """Main game loop"""
        print("Game started! Good luck!\n")
        
        while not self.game_logic.is_game_complete():
            # Get user input
            user_answer = self.screen.get_user_input(self.game_logic.get_score())
            
            # Check for exit
            if self.should_exit(user_answer):
                self.end_game()
                break
            
            # Process the guess
            self.process_guess(user_answer)
        
        # Check for victory
        if self.game_logic.is_game_complete():
            self.celebrate_victory()
        
        # Keep window open
        self.screen.keep_open()
    
    def should_exit(self, user_answer):
        """Check if user wants to exit"""
        return user_answer is None or user_answer.upper() == "EXIT"
    
    def process_guess(self, user_answer):
        """Process a user's guess"""
        # Look up the state
        state_row = self.state_data.find_state(user_answer)
        
        if state_row is None:
            # Not found
            print(f"✗ '{user_answer}' is not a valid state or abbreviation.\n")
            return
        
        # Get state info
        state_info = self.state_data.get_state_info(state_row)
        state_name = state_info['name']
        
        # Check if already guessed
        if self.game_logic.is_already_guessed(state_name):
            print(f"You already guessed {state_name}! Try another.\n")
            return
        
        # Correct guess!
        self.game_logic.add_guess(state_name)
        self.screen.write_state_name(state_name, state_info['x'], state_info['y'])
        print(f"✓ Correct! {state_name}")
        print(f"  Progress: {self.game_logic.get_score()}/50 states\n")
    
    def end_game(self):
        """Handle game ending"""
        score = self.game_logic.get_score()
        print(f"\nGame ended. You guessed {score} out of 50 states.")
        
        # Show missed states
        all_states = self.state_data.get_all_state_names()
        missed = self.game_logic.get_missed_states(all_states)
        if missed:
            print(f"\nMissed states ({len(missed)}):")
            for state in missed:
                print(f"  - {state}")
    
    def celebrate_victory(self):
        """Celebrate winning the game"""
        print("\n🎉 CONGRATULATIONS! You guessed all 50 states! 🎉")
        self.screen.show_victory()


def main():
    """Entry point for the game"""
    game = StatesGame()
    game.play()


if __name__ == "__main__":
    main()