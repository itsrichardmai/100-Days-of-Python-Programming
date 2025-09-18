# ============================================================================
# FUNCTION DESIGN AND ARCHITECTURE DECISION PROCESS
# Step-by-step explanation of how I decide program structure
# ============================================================================

"""
This demonstrates my thought process for designing functions and classes.
Let me walk through the Higher/Lower game as an example.
"""

# ============================================================================
# STEP 1: UNDERSTAND THE PROBLEM
# ============================================================================
"""
Higher/Lower Game Requirements:
1. Show two celebrities
2. Player guesses who has more followers
3. Track score
4. Continue until wrong guess
5. Show final score

First, I identify the MAIN ACTIONS (these become functions):
- Display game info
- Get two random people
- Show comparison
- Get user guess
- Check if guess is correct
- Update score
- Decide if game continues
"""

# ============================================================================
# STEP 2: IDENTIFY DATA AND BEHAVIOR
# ============================================================================
"""
DATA the game needs:
- List of celebrities
- Current score
- Current two people being compared
- Game state (playing/finished)

BEHAVIOR the game needs:
- Display information
- Make comparisons
- Track state
- Handle user input

This is WHY I chose a class - the game has both DATA and BEHAVIOR that belong together.
"""

# ============================================================================
# STEP 3: FUNCTION HIERARCHY - FROM BIG TO SMALL
# ============================================================================

# LEVEL 1: HIGHEST LEVEL - What the user sees
def main():
    """
    TOP LEVEL: The entry point
    - This just starts the game
    - Keeps the main logic simple
    """
    game = HigherLowerGame()
    game.play_game()

class HigherLowerGame:
    """
    WHY A CLASS?
    1. Game has STATE (score, current players, data)
    2. Game has BEHAVIOR (display, compare, validate)
    3. State and behavior are tightly coupled
    4. We might want multiple games or game sessions
    5. Easier to extend (add difficulty levels, different game modes)
    """
    
    def __init__(self):
        # Initialize GAME STATE
        self.score = 0
        self.game_data = []  # Will hold celebrity data
        self.is_game_over = False
        self.current_person_a = None
        self.current_person_b = None

    # LEVEL 2: MAIN GAME FLOW
    def play_game(self):
        """
        MAIN GAME LOOP - orchestrates the whole game
        WHY this function wraps others:
        - Controls the overall flow
        - Handles the game loop
        - Decides when game ends
        """
        self.display_welcome()        # Show intro
        self.load_game_data()         # Load celebrity data
        
        while not self.is_game_over:
            self.play_round()         # Play one round
        
        self.display_final_score()    # Show results

    # LEVEL 3: ROUND MANAGEMENT
    def play_round(self):
        """
        SINGLE ROUND LOGIC - wraps the actions of one round
        WHY separate from play_game():
        - Single Responsibility: only handles ONE round
        - Reusable: could be called from different contexts
        - Testable: easy to test one round in isolation
        """
        self.setup_round()           # Get two celebrities
        self.display_comparison()    # Show A vs B
        user_guess = self.get_user_guess()  # Get player input
        
        if self.is_guess_correct(user_guess):
            self.handle_correct_guess()
        else:
            self.handle_wrong_guess()

    # LEVEL 4: SPECIFIC ACTIONS
    def setup_round(self):
        """
        ROUND SETUP - prepares data for one round
        WHY separate function:
        - Single purpose: just get two different people
        - Reusable: might be called from different game modes
        - Validates data: ensures we have different people
        """
        self.current_person_a = self.get_random_person()
        self.current_person_b = self.get_random_person()
        
        # Ensure they're different
        while self.current_person_a == self.current_person_b:
            self.current_person_b = self.get_random_person()

    def display_comparison(self):
        """
        DISPLAY LOGIC - shows the comparison to user
        WHY separate:
        - UI responsibility only
        - Easy to change display format
        - Could be swapped for GUI version
        """
        print(f"A: {self.format_person(self.current_person_a)}")
        print("VS")
        print(f"B: {self.format_person(self.current_person_b)}")

    def get_user_guess(self):
        """
        INPUT HANDLING - gets and validates user input
        WHY separate:
        - Input validation in one place
        - Reusable for different input needs
        - Easy to add more validation rules
        """
        while True:
            guess = input("Who has more followers? (A or B): ").upper().strip()
            if guess in ['A', 'B']:
                return guess
            print("Please enter A or B only!")

    def is_guess_correct(self, guess):
        """
        GAME LOGIC - determines if guess is right
        WHY separate:
        - Core game logic in one place
        - Easy to modify comparison rules
        - Testable in isolation
        """
        a_followers = self.current_person_a['follower_count']
        b_followers = self.current_person_b['follower_count']
        
        if guess == 'A':
            return a_followers > b_followers
        else:
            return b_followers > a_followers

    # LEVEL 5: HELPER FUNCTIONS - Smallest, most specific
    def get_random_person(self):
        """
        UTILITY FUNCTION - single, simple task
        WHY separate:
        - Might be used multiple times
        - Could be enhanced (weighted random, categories)
        - Easy to test
        """
        import random
        return random.choice(self.game_data)

    def format_person(self, person):
        """
        FORMATTING HELPER - just formats display
        WHY separate:
        - Single responsibility
        - Easy to change format
        - Reusable across different displays
        """
        return f"{person['name']}: {person['description']}"

    def handle_correct_guess(self):
        """WHY separate: Groups related actions for correct guesses"""
        self.score += 1
        print(f"Correct! Score: {self.score}")

    def handle_wrong_guess(self):
        """WHY separate: Groups related actions for wrong guesses"""
        self.is_game_over = True
        print(f"Wrong! Final score: {self.score}")
        self.show_correct_answer()

    def show_correct_answer(self):
        """WHY separate: Specific display logic for answers"""
        a_count = self.current_person_a['follower_count']
        b_count = self.current_person_b['follower_count']
        print(f"A had {a_count:,} followers")
        print(f"B had {b_count:,} followers")

# ============================================================================
# MY DECISION PROCESS - THE MENTAL FRAMEWORK
# ============================================================================

"""
STEP 1: START WITH THE BIG PICTURE
- What is the main flow? (play_game)
- What are the major phases? (welcome -> rounds -> end)

STEP 2: BREAK DOWN EACH PHASE
- What happens in a round? (setup -> display -> input -> check -> respond)
- What data is needed at each step?

STEP 3: IDENTIFY REPEATED ACTIONS
- Getting random person -> separate function
- Formatting display -> separate function
- Validating input -> separate function

STEP 4: GROUP RELATED DATA AND BEHAVIOR
- Score, game state, current players = Game class
- Display logic = methods in Game class
- Game flow = methods in Game class

STEP 5: APPLY DESIGN PRINCIPLES

Single Responsibility Principle:
- Each function does ONE thing well
- get_user_guess() only handles input
- format_person() only formats display
- is_guess_correct() only checks logic

Don't Repeat Yourself (DRY):
- format_person() used multiple times
- get_random_person() used multiple times
- Input validation in one place

Separation of Concerns:
- Display logic separate from game logic
- Input handling separate from validation
- Data management separate from presentation

Easy to Test:
- Small functions are easy to test
- Pure functions (given input X, always return Y)
- Clear dependencies

Easy to Modify:
- Change display format? Only modify format_person()
- Change game rules? Only modify is_guess_correct()
- Add difficulty levels? Extend the class
"""

# ============================================================================
# WHY CLASS vs FUNCTIONS? - DECISION MATRIX
# ============================================================================

"""
USE A CLASS WHEN:
✅ You have data that needs to persist between function calls (score, game state)
✅ You have behavior that operates on that data (update score, check game state)
✅ You might want multiple instances (multiple games, different players)
✅ You want to group related functionality together
✅ You might extend the functionality later (inheritance)

USE FUNCTIONS WHEN:
✅ Simple, stateless operations (calculate tax, format string)
✅ Utility functions (math operations, file reading)
✅ One-time operations (data processing scripts)
✅ When you don't need to maintain state between calls

HIGHER/LOWER GAME ANALYSIS:
- Has persistent state ✅ (score, current comparison)
- Has related behavior ✅ (display, compare, validate)
- Might want multiple instances ✅ (different players/sessions)
- Will likely be extended ✅ (difficulty levels, categories)
- Groups related functionality ✅

CONCLUSION: Class is the right choice!
"""

# ============================================================================
# ALTERNATIVE: FUNCTION-BASED APPROACH (for comparison)
# ============================================================================

def functional_approach():
    """
    This shows what the game would look like with just functions.
    Notice how we have to pass game state around constantly.
    """
    
    def play_functional_game():
        score = 0
        game_data = load_game_data()
        display_welcome()
        
        while True:
            person_a, person_b = setup_round(game_data)
            display_comparison(person_a, person_b)
            guess = get_user_guess()
            
            if is_guess_correct(person_a, person_b, guess):
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Final score: {score}")
                break
    
    # Notice: We have to pass score, game_data around everywhere
    # The class approach keeps this data organized and accessible

"""
SUMMARY OF MY PROCESS:

1. IDENTIFY THE MAIN GOAL (play a guessing game)
2. BREAK INTO LOGICAL PHASES (setup -> play -> end)
3. IDENTIFY DATA THAT PERSISTS (score, game state)
4. GROUP RELATED DATA AND BEHAVIOR (class)
5. BREAK BEHAVIOR INTO SINGLE-PURPOSE FUNCTIONS
6. ORGANIZE BY HIERARCHY (high-level calls low-level)
7. MAKE EACH FUNCTION TESTABLE AND REUSABLE
8. APPLY DESIGN PRINCIPLES (SRP, DRY, separation of concerns)

The result: Clean, maintainable, extensible code!