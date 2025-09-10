import random 
from art import logo

def display_welcome():
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 - 100")
    print(logo)

def main():
    display_welcome()
    number = random.randint(1,100)
    lives = 0
    # print(number)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
    if difficulty == 'easy': 
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else: 
        print("Invalid Option!")
    while lives > 0: 
        print(f"you have {lives} lives remaining!")
        user_guess = int(input("Guess a number between 1 to 100!"))
        if user_guess > number:
            print("You guessed too high! The number is lower")
            lives -= 1 
        elif user_guess < number: 
            print("Your guessed too low! The number is higher!")
            lives -= 1 
        elif user_guess == number:
            print(f"You win! The number was {number}")
            return
        if lives == 0:
            print(f"You lost! The number was {number}")
            return
        
if __name__ == '__main__':
    main()


