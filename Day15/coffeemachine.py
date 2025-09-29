class CoffeeMachine:

    # Global constants for recipes of drinks
    ESPRESSO = {"cost": 1.50, "water":50, "coffee":18}
    LATTE = {"cost": 2.50, "water":200, "coffee":24, "milk":150}
    CAPPUCCINO = {"cost": 3.00, "water":250, "coffee":24, "milk":100}

    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 25
        self.turned_on = True 

    def display_report(self):
        print(f"""\n
        =======
        Machine contains:
        Water: {self.water}ML
        Milk: {self.milk}ML
        Money: ${self.money}
        TurnedOn: {self.turned_on}
        ========\n
        """)

    def get_user_choice(self):    
        choice = str(input("What would you like? (espresso/latte/cappucino)")).lower().strip()
        if choice == 'off':
            self.turned_on = False
            print("Turning off coffee machine. Goodbye!")
            return 'off'
        
        elif choice == 'report':
            self.display_report()
            return 'report'
        elif choice in ['espresso', 'latte',' cappuccino']:
            return choice
        else: 
            print("❌ Invalid choice. Please try again.")
            return 'invalid'
    def check_resources(self, drink_choice):
        # Check if enough resources are available for the selected drink
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
        
    def process_payment(self, cost):
        """Handle coin insertion and payment processing."""
        print(f"\n💰 Cost: ${cost:.2f}")
        print("Please insert coins:")
        
        try:
            quarters = int(input("How many quarters ($0.25)? ")) * 0.25
            dimes = int(input("How many dimes ($0.10)? ")) * 0.10
            nickels = int(input("How many nickels ($0.05)? ")) * 0.05
            pennies = int(input("How many pennies ($0.01)? ")) * 0.01
            
            total_inserted = quarters + dimes + nickels + pennies
            print(f"\n💵 You inserted: ${total_inserted:.2f}")
            
            if total_inserted >= cost:
                change = total_inserted - cost
                if change > 0:
                    print(f"💰 Here's your change: ${change:.2f}")
                
                # Add money to machine
                self.money += cost
                return True
            else:
                shortage = cost - total_inserted
                print(f"❌ Insufficient funds! Short ${shortage:.2f}. Money refunded.")
                return False
                
        except ValueError:
            print("❌ Invalid input. Please enter whole numbers only. Money refunded.")
            return False
    def make_drink(self, drink):
        """Prepare the selected drink and deduct resources."""
        if drink == 'espresso':
            recipe = self.ESPRESSO
        elif drink == 'latte':
            recipe = self.LATTE
        elif drink == 'cappuccino':
            recipe = self.CAPPUCCINO
        else:
            return False

        # Deduct resources
        self.water -= recipe['water']
        self.coffee -= recipe['coffee']
        
        if 'milk' in recipe:
            self.milk -= recipe['milk']

        print(f"☕ Here's your {drink}! Enjoy! ☕")
        return True

    
    def turn_on(self):
        """Main coffee machine operation loop."""
        print("☕ Welcome to the Coffee Machine!")
        while self.turned_on: 
            choice = self.get_user_choice()
        
            if choice in ['off', 'report']:
                continue
            
            if choice in ['espresso', 'latte', 'cappuccino']:
                # Step 1 check if we have enough resources
                # If check_resources returns not true, prompt user that we do not have enough resources
                if not self.check_resources(choice):
                    print("Please refill the machine or choose another drink!")
                    continue
            if choice == 'espresso':
                cost = self.ESPRESSO['cost']
            elif choice == 'latte':
                cost = self.LATTE['cost']
            else:
                cost = self.CAPPUCCINO['cost']
            # Process payment
            if self.process_payment(cost):
                # Make the drink
                self.make_drink(choice)
                print("Transaction complete! Here is your drink!")
            else:
                print("Transaction cancelled!")

print("\n☕ Coffee machine is now OFF. Have a great day! ☕")

def main():
    """Main function to run the game"""
    # Option 1: Using the class (Object-Oriented approach)
    coffee = CoffeeMachine()  # Create an instance of the class
    coffee.turn_on()
    # Option 2: Using functions (Procedural approach)
    # display_welcome_function()  # Call function directly

if __name__ == '__main__':
    main()
