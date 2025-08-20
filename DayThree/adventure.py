print('''
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      ''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
choice1 = input("You're are at a crossroad, where do you want to go? Type left or right? ").lower().strip()

if choice1 == 'left':
    choice2 = input('You\'ve come to a lake.\n'
          'There is an island in the middle of the lake.\n'
          'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower().strip()
    if choice2 != 'wait':
         print("Oh no! You swam and were eaten by a Shark! Game Over! ")
    else:
        choice3 = input("You made it to the island!\n" 
                      "There is a house with 3 doors: Red, Blue and Yellow.\n"
                      "Choose one of the doors. ").lower().strip()
        if choice3 == 'red':
            print("It's a room full of fire. Game Over! ")
        elif choice3 == "yellow":
            print(" You found the treasure! You win! " )
        elif choice3 == "blue": 
            print("A tiger comes out and eats you! Game Over! ")
        else:
            print("You did not choose a door in time and the house blew up! Game Over!")
else: 
    print("You died! Game Over!" )
