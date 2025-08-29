import random

# Start
words = ["Chicken", "Banana", "Rice", "Pudding"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
# Generate random word 
print(logo)
lives = 6
chosen_word = random.choice(words).lower()
# print(chosen_word)
# fill random word with placeholders to display random word 
placeholder = "" 
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#  Ask user to guess a letter 
# handle logic based on correct or incorrect 

game_over = False
correct_letters = []

while not game_over: 
    print(f"********************************Lives left: {lives}********************************")
    guess = str(input("HANGMAN: Guess a letter! ")).lower()
    display = ""
    print(stages[lives])
    for letter in chosen_word: 
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters: 
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word! You lost a life!") 
    if lives == 0:
        game_over = True
        print(f"You lose! The word was {chosen_word}")    

    if "_" not in display:
        game_over = True 
        print(f"You won! The word was {chosen_word}!" )

# Create a "display" that puts the guess letter in the right positions and _ 




# Condition for gameover to exit the while loop.
    