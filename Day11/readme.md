# Black Jack Game

<!-- Print logo & welcome to game 
<!-- Ask user for bet amount -->
<!-- Generate random card for player & one faceup card for dealer  -->

# My Decision Framework:
# 1. Single Responsibility Principle
Each class should have one main job:

Card: Represent a playing card
Hand: Manage a collection of cards
Player: Handle money and betting
Game: Orchestrate the overall flow

# 2. Data + Behavior Together
The class that owns the data should have the methods that work on that data:

class Player:
    def __init__(self):
        self.money = 1000        # Player owns money data
    
    def place_bet(self, amount): # Player handles money behavior
        if amount <= self.money:
            self.money -= amount
            return True
        return False

# 3. Minimize Dependencies
Classes should know as little as possible about each other:

Card doesn't need to know about Hand
Hand doesn't need to know about Player
Player doesn't need to know about Deck

Real Examples from Our Blackjack Game:
"Where should Ace conversion logic go?"
🤔 Options: Card class, Hand class, Game class
✅ My choice: Hand class
Why?

Hand has all the cards and knows the total
Hand naturally manages its own value
Card class stays simple and reusable
Easy to test: hand.get_value()

"Where should win/loss determination go?"
🤔 Options: Player class, Hand class, Game class
✅ My choice: Game class
Why?

Game knows all the rules
Game can see both player and dealer hands
Game controls payouts
Player and Hand classes stay focused

"Where should betting validation go?"
🤔 Options: Game class, Player class, separate Validator class
✅ My choice: Player class
Why?

Player owns their money
Player knows their betting limits
Encapsulates player state
Natural: player.place_bet(amount)

# My Step-by-Step Process:
When I encounter new functionality, I ask:

What data does this need?
Who owns that data?
Is this a core responsibility or a side effect?
How can I minimize dependencies?
Will this be easy to test?
Can this be reused elsewhere?

Common Mistakes I Avoid:
❌ God Object: One class doing everything
❌ Anemic Objects: Classes with data but no behavior
❌ Tight Coupling: Classes knowing too much about each other
❌ Wrong Abstraction Level: Mixing high and low-level concerns

# The Beautiful Result:
When done right, you get:

Clear responsibilities: Each class has an obvious purpose
Easy testing: Test each piece independently
Reusable code: Classes work in other contexts
Maintainable: Changes are localized
Understandable: Code reads like the real world

