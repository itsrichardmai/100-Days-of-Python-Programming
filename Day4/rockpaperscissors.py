import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computerchoice = random.choice([0,1,2])
rps = [rock, paper, scissors]
print("computer chose: ", rps[computerchoice])
print("you chose: ", rps[choice])

if choice >= 3 or choice < 0:
    print("You picked an invalid number! You lose!")
elif choice == 0 and computerchoice == 2:
    print("You win!")
elif choice == 2 and computerchoice == 0:
    print("You lost!")
elif computerchoice > choice:
    print("You lose!")
elif choice > computerchoice:
    print("You win!")
elif computerchoice == choice:
    print("It's a draw")

# if choice >= 3 or choice <0: 
#     print("You typed an invalid number. You lose!")
# elif choice == 0 and computerchoice == 2:
#     print("You win!")
# elif computerchoice == 0 and choice == 2:
#     print("You lose!")
