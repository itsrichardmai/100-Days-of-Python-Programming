class CoffeeMachine:
    """A coffee machine simulator with proper input handling and reporting."""

    # Global constants for recipes of drinks
    ESPRESSO = {"cost": 1.50, "water": 50, "coffee": 18}
    LATTE = {"cost": 2.50, "water": 200, "coffee": 24, "milk": 150}
    CAPPUCCINO = {"cost": 3.00, "water": 250, "coffee": 24, "milk": 100}

    def __init__(self):
        """Initialize the coffee machine with default resources."""
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 25
        self.turned_on = True 
        
    def display_report(self):
        """Display current resource levels and machine status."""
        print(f"""
=======
Report: 
Water: {self.water}ML
Milk: {self.milk}ML
Coffee: {self.coffee}G
Money: ${self.money}
Turned On: {self.turned_on}
========
        """)

    def get_user_choice(self):
        """Get and process user input for coffee machine operations."""
        # ✅ FIXED: Remove .split() and handle input as string
        choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower().strip()
        
        # ✅ FIXED: Return the choice so calling function knows what to do
        if choice == 'off':
            self.turned_on = False
            print("Turning off coffee machine. Goodbye!")
            return 'off'
        elif choice == 'report':
            self.display_report()
            return 'report'  # Return so we know report was shown
        elif choice in ['espresso', 'latte', 'cappuccino']:
            return choice
        else:
            print("❌ Invalid choice. Please try again.")
            return 'invalid'

    def check_resources(self, drink_choice):
        """Check if enough resources are available for the selected drink."""
        if drink_choice == 'espresso':
            recipe = self.ESPRESSO
        elif drink_choice == 'latte':
            recipe = self.LATTE
        elif drink_choice == 'cappuccino':
            recipe = self.CAPPUCCINO
        else:
            return False
        
        # Check water
        if self.water < recipe['water']:
            print("❌ Sorry, not enough water!")
            return False
        
        # Check coffee
        if self.coffee < recipe['coffee']:
            print("❌ Sorry, not enough coffee!")
            return False
        
        # Check milk (if needed)
        if 'milk' in recipe and self.milk < recipe['milk']:
            print("❌ Sorry, not enough milk!")
            return False
        
        return True

    def process_coins(self, cost):
        """Process coin payment from user."""
        print(f"Please insert coins. Cost: ${cost:.2f}")
        
        try:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickels = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
            
            total = quarters + dimes + nickels + pennies
            print(f"Total inserted: ${total:.2f}")
            
            if total >= cost:
                change = total - cost
                if change > 0:
                    print(f"Here's ${change:.2f} in change.")
                self.money += cost
                return True
            else:
                print("❌ Insufficient funds. Money refunded.")
                return False
                
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            return False

    def make_coffee(self, drink_choice):
        """Make the selected coffee drink."""
        if drink_choice == 'espresso':
            recipe = self.ESPRESSO
        elif drink_choice == 'latte':
            recipe = self.LATTE
        elif drink_choice == 'cappuccino':
            recipe = self.CAPPUCCINO
        else:
            return False
        
        # Deduct resources
        self.water -= recipe['water']
        self.coffee -= recipe['coffee']
        if 'milk' in recipe:
            self.milk -= recipe['milk']
        
        print(f"☕ Here's your {drink_choice}. Enjoy!")
        return True

    def turn_on(self):
        """Main coffee machine operation loop."""
        print("☕ Welcome to the Coffee Machine!")
        
        while self.turned_on: 
            # ✅ FIXED: Handle the return value from get_user_choice()
            choice = self.get_user_choice()
            
            # Skip processing if choice was 'report', 'off', or 'invalid'
            if choice in ['report', 'off', 'invalid']:
                continue
            
            # Process coffee orders
            if choice in ['espresso', 'latte', 'cappuccino']:
                # Check if resources are sufficient
                if not self.check_resources(choice):
                    continue
                
                # Get the cost for the drink
                if choice == 'espresso':
                    cost = self.ESPRESSO['cost']
                elif choice == 'latte':
                    cost = self.LATTE['cost']
                else:  # cappuccino
                    cost = self.CAPPUCCINO['cost']
                
                # Process payment
                if self.process_coins(cost):
                    self.make_coffee(choice)
                else:
                    continue
        
        print("Coffee machine is now off. Have a great day!")


# Alternative: Simpler version for testing just the report function
class SimpleCoffeeMachine:
    """Simplified version to demonstrate the fix."""
    
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 25
        self.turned_on = True

    def display_report(self):
        print(f"""
=======
Report: 
Water: {self.water}ML
Milk: {self.milk}ML
Coffee: {self.coffee}G
Money: ${self.money}
========
        """)

    def get_user_choice(self):
        # ✅ The key fix: don't use .split(), handle as string
        choice = input("Enter command (report/off): ").lower().strip()
        return choice  # Return the choice

    def turn_on(self):
        print("Simple Coffee Machine ON")
        
        while self.turned_on:
            choice = self.get_user_choice()  # Get the choice
            
            if choice == 'off':
                self.turned_on = False
                print("Machine OFF")
            elif choice == 'report':
                self.display_report()  # This will work now!
            else:
                print("Unknown command")


def main():
    """Main function to run the coffee machine."""
    print("Choose version:")
    print("1. Full Coffee Machine")
    print("2. Simple Coffee Machine (for testing)")
    
    try:
        version = int(input("Enter choice (1 or 2): "))
        if version == 1:
            coffee = CoffeeMachine()
            coffee.turn_on()
        elif version == 2:
            coffee = SimpleCoffeeMachine()
            coffee.turn_on()
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")


if __name__ == '__main__':
    main()